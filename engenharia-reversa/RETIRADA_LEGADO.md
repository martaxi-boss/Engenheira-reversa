# Registo de retirada do REA legado — 30/10/2026

## Identidades separadas

- **Preservado — motor FINAL:** `/home/ubuntu/rea-original-upstream-680`, commit do autor `160d821ac9a0310afcb8d1fc427862dd6508add5`, runtime próprio `/home/ubuntu/rea-final-runtime`.
- **Retirado — instalação antiga:** `/opt/rea-reversa` e serviços `rea-reversa-mcp.service` / `rea-mcp-oauth.service`.
- O código original do autor declara `6.8.0` como versão de pacote, mas a sua instalação final é distinta da instalação antiga apagada.

## Provas verificadas

1. A migração de dependências e fornecedores para o runtime do projeto final foi comprovada nos runs [40968620168](https://github.com/martaxi-boss/VPS/actions/runs/40968620168), [40969647492](https://github.com/martaxi-boss/VPS/actions/runs/40969647492) e [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346).
2. O motor final passou testes de health [40974869693](https://github.com/martaxi-boss/VPS/actions/runs/40974869693) e análise Android [40974717355](https://github.com/martaxi-boss/VPS/actions/runs/40974717355) antes da retirada.
3. Em 30/10/2026, capturas do terminal do proprietário confirmaram a desativação dos dois serviços antigos, ausência de processos, eliminação de `/opt/rea-reversa`, sucesso da CLI `providers --json` *após* remoção e cerca de **29 GB livres** na VPS. Estas capturas não são um novo run do GitHub Actions.

## GitHub

- Removidas apenas da árvore Git atual as pastas `rea/` e `certifications/`, e cinco referências de submódulos antigos em `.gitmodules`.
- Preservados `engenharia-reversa/`, submódulo `engenharia-reversa/original`, Skill, testes, workflow existente de validação e evidências históricas nos relatórios.
- A ponte operacional continua em `martaxi-boss/VPS`, branch `rea/one-skill-bridge-20261023` — não confundir esse nome com dependência do legado.
- **Sem reescrita de histórico, sem force push:** eliminar do HEAD não elimina imediatamente objetos e espaço do histórico remoto do GitHub.

## Limitações

Os ensaios da CLI não certificam cada ferramenta MCP, fornecedores comerciais, sessão gráfica ou dispositivos não ligados. O código original e os fornecedores independentes do motor final permanecem preservados.
