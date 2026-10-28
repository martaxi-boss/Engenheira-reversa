# Engenharia reversa

Este repositório mantém na pasta [rea](rea/) uma cópia **byte-exata do código-fonte** do lançamento oficial [REA 6.8.0](https://github.com/morluto/rea), importada do commit \`160d821ac9a0310afcb8d1fc427862dd6508add5\`.

- Fonte: https://github.com/morluto/rea
- Licença original: [MIT](rea/LICENSE)
- Guia do motor: [README REA](rea/README.md)

Os caminhos dos cinco submódulos originais são adaptados no \`.gitmodules\` da raiz. A ligação ChatGPT/GitHub/SSH à VPS reside noutro repositório e não altera o código do autor.

A igualdade aqui verificada é do código-fonte; a ativação do motor da VPS e as respetivas dependências são tratadas separadamente.

## Certificações funcionais — REA 6.8.0

**Estado validado:** 150 ferramentas MCP a verde no âmbito realmente testado (125 anteriores + 25 novas); 79 pendentes num catálogo de 229.

- [Registo canónico das 229 ferramentas com estado individual e proveniência](certifications/rea-6.8.0.json).
- [Registo operacional e provas históricas no repositório VPS](https://github.com/martaxi-boss/VPS/blob/98f7bb3a4a6ecd262d25aa2fc7edae9a1e3ad929/rea-linux/certification/functional-ledger.json).
- [Relatório da meta de 150](https://github.com/martaxi-boss/VPS/blob/98f7bb3a4a6ecd262d25aa2fc7edae9a1e3ad929/rea-linux/certification/priority4-target150-batch-f-final-20261028.json).

**Verde significa certificação limitada ao cenário comprovado.** Não significa certificação de fornecedores pagos, funcionalidades não testadas ou ferramentas exclusivas de outros sistemas operativos. Não há qualquer importação automática de certificações da versão 6.7.0. O código original de 6.8.0 na pasta `rea/` mantém-se byte-exato e não foi modificado.
