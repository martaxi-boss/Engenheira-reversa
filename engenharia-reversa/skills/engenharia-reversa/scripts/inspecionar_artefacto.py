#!/usr/bin/env python3
"""Inventário estritamente de leitura de um artefacto, sem extrair nem executar.

Uso: python3 inspecionar_artefacto.py FICHEIRO [--output NOVO.json]
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile

MAX_ENTRIES_TO_REPORT = 100
MAX_MEMBERS_TO_SCAN = 100000


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def format_guess(head, name):
    lower = name.lower()
    if head.startswith(b"\x7fELF"):
        return "ELF"
    if head.startswith(b"MZ"):
        return "PE/DOS (cabecalho MZ; PE ainda nao validado)"
    if head.startswith((b"\xfe\xed\xfa\xce", b"\xce\xfa\xed\xfe",
                       b"\xfe\xed\xfa\xcf", b"\xcf\xfa\xed\xfe",
                       b"\xca\xfe\xba\xbe")):
        return "Mach-O / Fat"
    if head.startswith(b"\x00asm"):
        return "WebAssembly"
    if head.startswith(b"\x1f\x8b"):
        return "gzip"
    if head.startswith(b"PK\x03\x04") or head.startswith(b"PK\x05\x06"):
        return "ZIP (potencial APK/JAR)" if lower.endswith((".apk", ".jar")) else "ZIP"
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return "PNG"
    if head.startswith(b"%PDF-"):
        return "PDF"
    if head.startswith(b"SQLite format 3\x00"):
        return "SQLite"
    return "nao_identificado"


def zip_inventory(path):
    out = {"arquivo_zip_valido": False, "ficheiros_amostrados": [], "avisos": []}
    if not zipfile.is_zipfile(path):
        out["avisos"].append("assinatura ZIP encontrada mas estrutura nao validada")
        return out
    with zipfile.ZipFile(path, "r") as archive:
        entries = archive.infolist()
        out["arquivo_zip_valido"] = True
        out["total_entradas"] = len(entries)
        if len(entries) > MAX_MEMBERS_TO_SCAN:
            out["avisos"].append("muitas entradas; verificacao limitada")
        total_uncompressed = 0
        total_compressed = 0
        suspicious = 0
        encrypted = 0
        traverse = 0
        for i, z in enumerate(entries[:MAX_MEMBERS_TO_SCAN]):
            normalized = z.filename.replace("\\", "/")
            parts = PurePosixPath(normalized).parts
            bad_path = normalized.startswith("/") or bool(re.match(r"^[A-Za-z]:", normalized)) or ".." in parts
            if bad_path:
                traverse += 1
            if z.flag_bits & 1:
                encrypted += 1
            total_uncompressed += z.file_size
            total_compressed += z.compress_size
            if z.compress_size and z.file_size / z.compress_size > 1000:
                suspicious += 1
            if i < MAX_ENTRIES_TO_REPORT:
                out["ficheiros_amostrados"].append({
                    "nome": z.filename[:400],
                    "bytes_descomprimidos": z.file_size,
                    "bytes_comprimidos": z.compress_size,
                    "encriptado": bool(z.flag_bits & 1),
                    "caminho_suspeito": bool(bad_path),
                })
        out["total_bytes_descomprimidos_declarados"] = total_uncompressed
        out["total_bytes_comprimidos_declarados"] = total_compressed
        out["entradas_encriptadas"] = encrypted
        out["entradas_com_caminho_suspeito"] = traverse
        out["entradas_ratio_acima_1000"] = suspicious
        if traverse:
            out["avisos"].append("nomes potencialmente inseguros para extracao; nenhuma extracao foi feita")
        if suspicious or total_uncompressed > 10 * 1024**3:
            out["avisos"].append("potencial risco de descompressao excessiva; nenhuma extracao foi feita")
        if len(entries) > MAX_ENTRIES_TO_REPORT:
            out["avisos"].append("lista de membros truncada")
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ficheiro", type=Path)
    parser.add_argument("--output", type=Path, help="novo ficheiro JSON, sem substituir existentes")
    args = parser.parse_args()
    path = args.ficheiro
    if path.is_symlink():
        parser.error("nao analisar ligacoes simbolicas")
    try:
        info = path.stat()
    except OSError as exc:
        parser.error("ficheiro inacessivel: " + str(exc))
    if not stat.S_ISREG(info.st_mode):
        parser.error("esperado um ficheiro regular")
    if args.output and args.output.resolve() == path.resolve():
        parser.error("nao substituir o artefacto de entrada")
    with path.open("rb") as handle:
        head = handle.read(16)
    detected = format_guess(head, path.name)
    result = {
        "estado": "INVENTARIO_SEM_EXECUCAO",
        "caminho": str(path.resolve()),
        "tamanho_bytes": info.st_size,
        "sha256": sha256_file(path),
        "formato_provavel": detected,
        "executou_artefacto": False,
        "extraiu_artefacto": False,
        "limites": ["identificacao por assinatura inicial; requer verificacao especializada"],
    }
    if detected.startswith("ZIP"):
        try:
            result["zip"] = zip_inventory(path)
        except (zipfile.BadZipFile, OSError, ValueError) as exc:
            result["zip"] = {"arquivo_zip_valido": False,
                             "erro": type(exc).__name__ + ":" + str(exc)[:180]}
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        try:
            with args.output.open("x", encoding="utf-8") as handle:
                handle.write(output)
        except FileExistsError:
            parser.error("o relatorio ja existe; sem substituicao")
    else:
        print(output, end="")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError) as exc:
        print("ERRO=" + type(exc).__name__ + ":" + str(exc), file=sys.stderr)
        sys.exit(2)
