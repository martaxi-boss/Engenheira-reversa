# Ponte operacional verificada

Repositorio de transporte: `martaxi-boss/VPS`, branch `rea/one-skill-bridge-20261023`.
Workflow unico existente: `.github/workflows/rea-mcp-transport-20261027.yml`.
Pedido: `rea-linux/skill-requests/current.json`. Executador: `rea-linux/skill-bridge/execute_request.py`.
Modelo: `{"schema_version":1,"project":"engenharia-reversa-final","engine_commit":"160d821ac9a0310afcb8d1fc427862dd6508add5","request_id":"health-example-20261029","operation":"health"}`.
Operacoes: `health`, `providers`, `inspect_elf`, `apk_demo`. Sem paths e comandos arbitrarios.
Atualizar ficheiro pelo conector GitHub, branch e SHA do blob, mensagem `skill-request: <id>`; localizar execucao pelo novo commit SHA; ler job `engenharia-reversa-skill` e confirmar `REA_SKILL_BRIDGE_RESULT` com ID coincidente.
Prova de health: https://github.com/martaxi-boss/VPS/actions/runs/40961687695.
Os fornecedores nao sao reinstalados; alguns continuam partilhados com o REA legado.
