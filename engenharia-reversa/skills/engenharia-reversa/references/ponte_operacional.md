# Ponte real Engenharia Reversa FINAL

- Motor: checkout `morluto/rea`, commit original `160d821ac9a0310afcb8d1fc427862dd6508add5`, em `/home/ubuntu/rea-original-upstream-680`.
- Dependências e Node da CLI: `/home/ubuntu/rea-final-runtime`; não aceder a `/opt/rea-reversa`.
- Repositório de transporte: `martaxi-boss/VPS`.
- Branch operacional: `rea/one-skill-bridge-20261023`.
- Workflow existente: `.github/workflows/rea-mcp-transport-20261027.yml`.
- Request: `rea-linux/skill-requests/current.json`.
- Executor real na VPS (via SSH verificado): `rea-linux/skill-bridge/execute_request.py`.

## Catalogo e chamada dinamica do MCP ORIGINAL

A mesma ponte existente suporta `mcp_catalog`, `mcp_describe` e `mcp_call`. Nao utiliza uma lista manual de ferramentas: descobre os contratos do proprio checkout e interroga o servidor MCP original por stdio durante o trabalho. Nenhum MCP adicional e instalado.

A estrutura de pedido mantem cinco campos: `schema_version`, `project`, `engine_commit`, `request_id` e `operation`.

```json
{"schema_version":1,"project":"engenharia-reversa-final","engine_commit":"160d821ac9a0310afcb8d1fc427862dd6508add5","request_id":"rea-final-catalog-example-20261030","operation":"mcp_catalog"}
```

Para ver o esquema exato da ferramenta, escolher `operation:"mcp_describe"` e adicionar `"tool_name":"inspect_analysis_settings"`. Para a executar, escolher `operation:"mcp_call"` e adicionar `"tool_name":"inspect_analysis_settings","arguments":{}`. Os nomes sao exemplos: a escolha e dinamica a partir do catalogo original. Consultar primeiro o `input_schema` devolvido.

Ler `REA_SKILL_BRIDGE_RESULT` nos logs. `mcp_operation.status=PASS` e `mcp_operation.isError=false` sao necessarios para afirmar execucao da ferramenta. Confirmar `transport="original-mcp-stdio"`, `tool`, campos de resultado e tempo. Para ferramentas com efeitos sobre alvos, ficheiros ou dispositivos, a ponte devolve `BLOCKED`; estas exigem um fluxo de autorizacao especifico antes da sua execucao. Sessao, caminhos e fornecedores necessarios continuam sujeitos ao ambiente real.

Provas reais de 30/10/2026: catalogo 229 em [41027641420](https://github.com/martaxi-boss/VPS/actions/runs/41027641420), esquema MCP em [41028138424](https://github.com/martaxi-boss/VPS/actions/runs/41028138424), ferramenta MCP executada em [41028238883](https://github.com/martaxi-boss/VPS/actions/runs/41028238883).

## Contrato

Operações básicas: `health`, `providers`, `inspect_elf`, `apk_demo`, `isolation_audit`, `environment_audit`, `provider_diagnostics`, `strict_separation_audit`, `optional_source_symlinks`, `hygiene_inventory`.

Análise real de JavaScript de projeto público do proprietário:

```json
{
  "schema_version": 1,
  "project": "engenharia-reversa-final",
  "engine_commit": "160d821ac9a0310afcb8d1fc427862dd6508add5",
  "request_id": "rea-project-source-example-20261030",
  "operation": "analyze_project_javascript",
  "source_repo": "martaxi-boss/lowcost-europa",
  "revision": "28c998e88bb723424c8ed36d4ba93904339ec877",
  "javascript_dir": "apps/storefront/static/storefront",
  "source_paths": ["catalog-explorer.js", "product-images.js"]
}
```

Substituir `revision` pelo HEAD atual do GitHub e selecionar os ficheiros relevantes dentro da mesma pasta; nunca copiar cegamente o SHA do exemplo para um trabalho posterior. O servidor rejeita URLs fora do namespace, revisões não SHA-40, caminhos com `..`, ficheiros fora da pasta e diretórios/ficheiros simbólicos.

Fluxo obrigatório: GitHub `fetch_file` -> `update_file` (na branch operacional, com o SHA consultado, mensagem `skill-request: <request_id>`) -> localizar Actions pelo novo commit SHA -> `fetch_workflow_run_jobs` -> `fetch_workflow_job_logs` -> validar `REA_SKILL_BRIDGE_RESULT`.

Resultado real de referência: [41022019825](https://github.com/martaxi-boss/VPS/actions/runs/41022019825) `PASS` após correção do parâmetro obrigatório `--evidence_output` para o modo `--detail summary` da CLI do autor. A fonte é clonada para diretório temporário; a CLI executa a análise estática e devolve estrutura de Evidence, sem executar o JavaScript do alvo, sem alterar o projeto de produção e sem guardar cópias permanentes.

Relatórios devem indicar qual o comando da CLI realmente executado, os hashes, fornecedores usados, resultados e limites. Não usar o `health` ou o sucesso dos testes de outro projeto como prova de análise REA.
