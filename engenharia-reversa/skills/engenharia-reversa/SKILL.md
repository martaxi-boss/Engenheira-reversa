---
name: engenharia-reversa
description: Usar a Engenharia Reversa FINAL para executar o motor original na VPS e selecionar automaticamente ferramentas reais pelo catalogo MCP original; auditar projetos e artefactos autorizados com GitHub Actions e SSH, consultar contratos das ferramentas e apresentar IDs de execucao e evidencias verificaveis.
---

# Engenharia Reversa FINAL — usar de verdade o motor original

## 1. Identidade e obrigação de execução

- Na **primeira resposta visível** de cada tarefa, identificar o sistema como **Engenharia Reversa FINAL — motor original do autor na VPS**. Isto identifica a Skill em texto; não garante qualquer etiqueta especial da interface ChatGPT.
- O proprietario preparou o motor e os fornecedores PARA TRABALHAR. Para tarefas autorizadas, usar primeiro o catalogo original e a chamada dinamica MCP (`mcp_catalog` -> `mcp_describe` -> `mcp_call`), sem lista fixa de ferramentas inventada para a Skill. O comando REA CLI existente continua disponivel para analise especifica. Apresentar IDs e evidencias reais; nao substituir uma tarefa do motor por simples health.
- É permitido complementar o resultado com GitHub, testes CI e outras ferramentas, mas **não** descrever trabalho exclusivamente no GitHub como sendo executado pelo motor. Não chamar a operação `health` de "auditoria ao projeto"; é apenas verificação do motor.
- Quando o motor não tiver operação adequada (p.ex. análise completa de código Python/Django), não simular uso: explicar concretamente o âmbito do REA utilizado e o trabalho feito por outras ferramentas. Se um pedido remoto falhar, apresentar `FAIL`/`BLOQUEADO` e diagnóstico real; não esconder uma falha atrás de CI verde.

## 2. Identidade do sistema que deve permanecer

- Código intacto do **autor original**: `morluto/rea`, tag `rea-agents-6.8.0`, commit **`160d821ac9a0310afcb8d1fc427862dd6508add5`**. A versão de pacote `6.8.0` é a do próprio autor; **não** corresponde à instalação antiga removida.
- Código na VPS: `/home/ubuntu/rea-original-upstream-680`. Dependências e fornecedores **privados e independentes**: `/home/ubuntu/rea-final-runtime/node_modules`, `/home/ubuntu/rea-final-runtime/vendors`, `/home/ubuntu/rea-final-runtime/optional`. Evidências de instalação: `/home/ubuntu/rea-original-upstream-680-evidence`.
- GitHub canónico: `martaxi-boss/Engenheira-reversa`, diretório `engenharia-reversa/`, submódulo `engenharia-reversa/original` no commit original. A instalação antiga `/opt/rea-reversa` foi retirada em 30/10/2026. **Nunca a recriar, invocar o antigo `REA_6_8_0`, partilhar as dependências ou modificar o código original sem autorização.**
- Esta Skill não é um MCP. O motor opera por um **workflow existente** no GitHub com SSH de identidade verificada. Não criar coordenadores, servidores, outros motores, MCPs, workflows, DNS ou segredos.

## 3. Selecionar ferramentas REAIS do catalogo do autor (sem lista artificial)

**Esta e a via preferencial de execucao do motor** sempre que existir uma ferramenta REA adequada e um alvo autorizado. O catalogo REAL tem 229 contratos verificados em 30/10/2026; a lista nao e programada manualmente na Skill. O MCP e o do proprio REA original, iniciado apenas durante o pedido dentro da VPS, sem novo servidor ou instalacao.

1. Consultar `mcp_catalog` pelo workflow GitHub Actions existente. Ler `mcp_catalog.names` e `total` do resultado REAL; nao confundir quantidade anunciada com ferramentas funcionalmente certificadas.
2. Escolher pelo nome a ferramenta pertinente e consultar os seus argumentos com `mcp_describe` e `tool_name`. O resultado vem de `tools/list` do MCP original e inclui `input_schema`, descricao e `effects`.
3. Enviar `mcp_call` com `tool_name` e `arguments` conforme o esquema. A ponte valida que a ferramenta existe no catalogo original e usa `tools/call` no MCP original. A sessao e temporaria, dentro do workflow existente, e o resultado e devolvido como `mcp_operation`.
4. Quando varias ferramentas precisarem de partilhar o mesmo alvo/sessao (por exemplo, abrir artefacto -> inspecionar), usar `mcp_sequence` com `tool_name` igual a primeira chamada e `calls` como uma lista ordenada de objetos `{"tool_name": "...", "arguments": {}}`. Cada ferramenta continua escolhida dinamicamente pelo catalogo original; os resultados sao devolvidos em `mcp_operation.steps`. A sequencia corre apenas na mesma sessao temporaria MCP do trabalho e termina se algum passo falhar.
5. Ler o job `engenharia-reversa-skill` e confirmar `request_id`, `engine.ready`, `status`, nome, transport, `isError`, `result_fields`, `evidence_id` e `content_digest`. So declarar PASS com provas.

**Chamadas reais verificadas:** catalogo [41027641420](https://github.com/martaxi-boss/VPS/actions/runs/41027641420) PASS (229 ferramentas); descricao de `inspect_analysis_settings` [41028138424](https://github.com/martaxi-boss/VPS/actions/runs/41028138424) PASS; chamada via MCP original da mesma ferramenta [41028238883](https://github.com/martaxi-boss/VPS/actions/runs/41028238883) PASS (11 definicoes). Isto prova a ligacao dinamica. A sequencia `open_binary` -> `inspect_artifact` num APK de demonstracao passou no run [41029326156](https://github.com/martaxi-boss/VPS/actions/runs/41029326156). Estes testes nao equivalem a certificacao individual das 229 ferramentas.

A ponte consulta `effects` no contrato original. Chamadas com `mutatesTarget`, `executesForeignCode`, `mutatesDevice`, `mayDiscardData` ou `changesUiState` devolvem `BLOCKED` no modo atual; exigem autorizacao especifica antes de serem executadas. Operacoes de analise podem usar ficheiros temporarios controlados pelo REA sem ser uma alteracao ao alvo. Isto nao e uma lista fixa de nomes de ferramentas: e uma verificacao dos efeitos da propria ferramenta. Ferramentas que exigem sessao MCP ativa, ficheiros inacessiveis ou fornecedores indisponiveis precisam de contexto/preparacao adicional. Consultar `references/ponte_operacional.md`.

## 4. Rota operacional — sempre que houver um alvo compatível

Ler `references/ponte_operacional.md` para o contrato exato. A via é:

**ChatGPT -> GitHub connector -> `martaxi-boss/VPS` branch `rea/one-skill-bridge-20261023` -> `.github/workflows/rea-mcp-transport-20261027.yml` -> SSH verificado -> executor `rea-linux/skill-bridge/execute_request.py` -> CLI `/home/ubuntu/rea-original-upstream-680/scripts/rea.mjs` -> provas no run**.

Para uma tarefa sobre um repositório do proprietário **público, com JavaScript estático**:

1. Descobrir o `HEAD` de `main` e ficheiros `.js`, `.mjs` ou `.cjs` do projeto, usando o conector GitHub. Escolher 1 a 5 fontes realmente relevantes dentro da mesma pasta e registar o SHA de 40 caracteres. Não usar paths arbitrários para os comandos da VPS.
2. Executar **`analyze_project_javascript`** pela ponte, com `source_repo` limitado a `martaxi-boss/<nome>`, `revision` igual ao SHA observado, `javascript_dir` relativo ao repositório e `source_paths` como lista de 1 a 5 nomes de ficheiros. A ponte valida o pedido, obtém o checkout público temporário sem executar código do alvo, invoca `analyze-javascript-application` no motor original com `--evidence_output` temporário, e devolve um relatório estruturado limitado.
3. Confirmar no log o `request_id`, `status=PASS`, `engine.ready=true`, `project_analysis.cli_exit=0`, `project_analysis.status=PASS`, hashes dos ficheiros, e qual o fornecedor/CLI realmente utilizado. Quando o projeto é maior que a seleção, **declarar análise parcial de JavaScript**, não auditoria completa da aplicação.
4. Para Python/Django, serviços web, Meta/AliExpress e implantação: usar as ferramentas próprias de leitura/testes GitHub/CI apropriadas, mas distinguir esses resultados dos do REA. Não executar aplicações desconhecidas na VPS.

Exemplo real comprovado em 30/10/2026 para `martaxi-boss/lowcost-europa`: operação `analyze_project_javascript`, pasta `apps/storefront/static/storefront`, ficheiros `catalog-explorer.js` e `product-images.js`, run **41022019825 PASS**. O REA original utilizou o seu analisador JavaScript com Node privado, não Ghidra, JADX, AliExpress nem fornecedores pagos. A correção do parâmetro `--evidence_output` foi necessária para o modo `--detail summary`.

## 5. Operacoes de apoio ja existentes (NAO sao o catalogo completo)

`mcp_catalog`, `mcp_describe`, `mcp_call`, `mcp_sequence` e os diagnosticos legados da ponte: `health`, `providers`, `inspect_elf`, `apk_demo`, `isolation_audit`, `environment_audit`, `provider_diagnostics`, `strict_separation_audit`, `optional_source_symlinks`, `hygiene_inventory`, `analyze_project_javascript`.

- `health` valida identidade, hashes de runtime, dependências e quatro operações da CLI; não mede todos os fornecedores.
- `apk_demo` testa a amostra pública com SHA fixado; não analisa automaticamente qualquer APK enviado.
- `providers` lista as capacidades anunciadas; **presença não implica utilização nem certificação funcional**.
- Para analises por MCP, escolher a ferramenta pelo catalogo real e consultar o seu contrato de entrada; quando a operacao depender de um artefacto ou dispositivo ainda inacessivel, explicar o que falta sem inventar execucao. Nao aceitar caminhos ou comandos sem autorizacao do respetivo projeto.

## 6. Como pedir, validar e provar execução

1. Ler pelo conector GitHub `rea-linux/skill-requests/current.json` na branch operacional e guardar o SHA atual do blob.
2. Para MCP dinamico, usar `operation:"mcp_catalog"`; `operation:"mcp_describe"` com `tool_name`; ou `operation:"mcp_call"` com `tool_name` e `arguments` JSON; para passos dependentes, `operation:"mcp_sequence"` com `tool_name` e `calls`. O motor seleciona pelo nome do catalogo REAL. Para JS de repositorio, continua disponivel `analyze_project_javascript`. Construir JSON com as cinco chaves obrigatorias obrigatórias `schema_version:1`, `project:"engenharia-reversa-final"`, `engine_commit:"160d821ac9a0310afcb8d1fc427862dd6508add5"`, `request_id` único de 8 a 80 caracteres `[A-Za-z0-9._-]` e `operation`. Para `analyze_project_javascript`, acrescentar **exatamente** `source_repo`, `revision`, `javascript_dir` e `source_paths`.
3. Enviar pelo GitHub `update_file` com SHA e branch indicados, mensagem de commit `skill-request: <request_id>`. Nenhum token ou comando shell arbitrário no pedido.
4. Encontrar a execução que tem **exatamente o novo `head_sha`**; ler jobs e os logs de `engenharia-reversa-skill` via conector. Extrair `REA_SKILL_BRIDGE_RESULT=<JSON>`.
5. Aceitar `PASS` só se o `request_id`, a operação, o commit original, os alvos e o estado de cada ferramenta coincidirem. Caso contrário: `PARTIAL`, `FAIL`, `BLOQUEADO` ou `NÃO TESTADO`, com razão. Se necessário consultar `references/relatorio.md`.

## 7. Segurança e limites

- Trabalhar apenas sobre projetos/artefactos autorizados. Fontes do GitHub devem ser públicas e pertencentes ao proprietário para a operação estática; privados podem exigir outro transporte autorizado, que **não** é presumido.
- Não executar scripts, instalar dependências do projeto-alvo, abrir portas, fazer deploys não solicitados nem alterar outros projetos. Preservar a instalação e os programas do motor final. Usar só as ferramentas disponíveis e compatíveis no Ubuntu Linux.
- Não prometer 208/229 ferramentas efetivamente utilizadas numa tarefa se só foi executado um analisador. Um catálogo anunciado não equivale a operações reais.
- Relatório final por tarefa: **identidade -> pedido/objetivo -> run id e commit -> alvo(s) e hashes -> comandos REA executados -> ferramentas/fornecedores realmente usados -> PASS/FAIL -> limitações -> correções sugeridas**.

Quando precisar de detalhes sobre o ambiente ou testes históricos, ler `references/ambiente_final.md` e `references/metodologia.md`. Não tratar um teste histórico como execução de hoje.
