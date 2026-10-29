#!/usr/bin/env bash
# Install ONLY the new original-source workspace in a dedicated home directory.
set -euo pipefail
umask 077

EXPECTED_PIN="5f9187cd279084581fd8c333ba4c6c2c8c506c11"
OFFICIAL_URL="https://github.com/morluto/rea.git"
: "${HOME:?HOME nao definido}"

# Deliberately do not accept arbitrary target roots or perform sudo operations.
ROOT="${HOME}/engenharia-reversa-novo"
SOURCE="${ROOT}/source"

if [[ -L "${ROOT}" || -L "${SOURCE}" ]]; then
  echo "BLOCKED: ligacao simbolica no destino exclusivo" >&2
  exit 20
fi
if [[ -e "${SOURCE}" && ! -d "${SOURCE}/.git" ]]; then
  echo "BLOCKED: diretorio source existente nao e um checkout git valido" >&2
  exit 21
fi
mkdir -p "${ROOT}/state" "${ROOT}/cache" "${ROOT}/tmp" "${ROOT}/evidence"

if [[ ! -d "${SOURCE}/.git" ]]; then
  git clone --filter=blob:none --depth=1 "${OFFICIAL_URL}" "${SOURCE}"
fi
if [[ "$(git -C "${SOURCE}" remote get-url origin)" != "${OFFICIAL_URL}" ]]; then
  echo "BLOCKED: o checkout nao aponta para a fonte oficial" >&2
  exit 22
fi
if [[ -n "$(git -C "${SOURCE}" status --porcelain)" ]]; then
  echo "BLOCKED: checkout com alteracoes por preservar" >&2
  exit 23
fi

git -C "${SOURCE}" fetch --no-tags --depth=1 origin "${EXPECTED_PIN}"
git -C "${SOURCE}" checkout --detach "${EXPECTED_PIN}"
ACTUAL="$(git -C "${SOURCE}" rev-parse HEAD)"
if [[ "${ACTUAL}" != "${EXPECTED_PIN}" ]]; then
  echo "FAIL: commit original nao corresponde ao esperado" >&2
  exit 24
fi

test -f "${SOURCE}/scripts/rea.mjs"
test -f "${SOURCE}/package.json"
printf 'NOVO_ENGINE_SOURCE=PASS\nNOVO_ENGINE_PIN=%s\nNOVO_ENGINE_ROOT=%s\nNOVO_ENGINE_BUILD=NOT_TESTED\nNOVO_ENGINE_PROVIDERS=NOT_TESTED\n' "${ACTUAL}" "${ROOT}"
