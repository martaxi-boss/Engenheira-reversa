# Engenharia Reversa - projeto novo e isolado

Este projeto e **novo** e vive apenas em `engenharia-reversa/` no repositorio `martaxi-boss/Engenheira-reversa`. O projeto legado continua intacto na pasta `rea/`. **Nao utilizar executaveis, Node modules, bridge, servicos, chaves SSH, evidencias ou configuracoes da pasta antiga.**

## Fonte original, sem alteracoes

- Origem: https://github.com/morluto/rea.git
- Integracao: submodulo Git proprio em `engenharia-reversa/original/`.
- Commit original imutavel para este ensaio: `5f9187cd279084581fd8c333ba4c6c2c8c506c11`.
- O pacote upstream ainda usa a designacao de versao `6.8.0`; isso **nao** transforma a copia independente no projeto legado. A identidade e dada pelo commit original, pasta, configuracoes e instalacao isolados.
- Submodulo mantido no repositório para acesso a fonte original sem copiar nem modificar o codigo do autor.

Para preparar a fonte numa copia do repositorio:

```bash
git submodule update --init --depth 1 engenharia-reversa/original
python3 -m unittest discover -s engenharia-reversa/tests -p 'test_*.py' -v
bash -n engenharia-reversa/scripts/vps_install.sh
```

## VPS: instalacao independente

- Destino exclusivo: `/home/ubuntu/engenharia-reversa-novo/`, para o utilizador `ubuntu`.
- Fonte: `/home/ubuntu/engenharia-reversa-novo/source/` (checkout limpo diretamente do upstream no commit acima).
- Dados, cache, temporarios e evidencias: `state/`, `cache/`, `tmp/`, `evidence/` dentro da pasta exclusiva.
- O script `scripts/vps_install.sh` e idempotente e nao requer root; verifica a identidade do checkout e nao executa nem instala os fornecedores pagos ou incompatíveis.
- O script preserva integralmente os outros diretorios do servidor. Nao reutiliza o motor antigo.

## GitHub Actions e ligacao SSH

O workflow separado `.github/workflows/engenharia-reversa-novo.yml` testa apenas a arvore nova e o submodulo oficial. Para ligar a VPS utiliza **somente** a configuracao dedicada ao projeto novo:

- Secret: `ENG_REV_VPS_SSH_KEY` (chave privada SSH para este projeto).
- Vars: `ENG_REV_VPS_HOST`, `ENG_REV_VPS_USER` e `ENG_REV_VPS_HOST_PIN` (fingerprint SHA256 Ed25519 verificado de antemao).
- Deploy de VPS nunca corre num push normal: requer execucao manual `workflow_dispatch` com `vps_install=true` e configuracao SSH valida.

Nenhuma chave, host, segredo, workflow, motor ou certificado do legado e copiado para o projeto novo. Um sucesso no teste de estrutura **nao** representa descompilacao avancada, certificacao de fornecedores ou VPS instalada.

## Criterios para considerar novo operacional

1. Estrutura GitHub e commit oficial imutavel: verificar no workflow novo.
2. Instalacao separada na VPS: instalacao via SSH dedicado e read-back verificavel.
3. Dependencias de compilacao e fornecedores: inventario e ensaios reais **deste** ambiente.
4. Motor e CLI: comandos e testes reais sobre amostras controladas, incluindo descompilacao quando suportada.
5. Skill ChatGPT: apontar exclusivamente para este projeto e demonstrar chamada real.
6. Nenhuma regressao ou dependencia do legado. **Nunca apagar o legado antes de ordem expressa do proprietario.**
