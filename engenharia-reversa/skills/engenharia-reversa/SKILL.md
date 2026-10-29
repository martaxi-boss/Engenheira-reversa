---
name: engenharia-reversa
description: Usar a Engenharia Reversa para auditar, descompilar e investigar software autorizado, e para consultar ou operar de forma verificada o motor original FINAL instalado na VPS em /home/ubuntu/rea-original-upstream-680, com fonte fixada em 160d821ac9a0310afcb8d1fc427862dd6508add5 e registo no GitHub martaxi-boss/Engenheira-reversa/engenharia-reversa. Usar para APK, ELF, PE, ZIP, firmware, comparacao de versoes, erros, fornecedores e verificacao de isolamento. Nunca confundir o motor final com o projeto legado na pasta rea/.
---

# Engenharia Reversa

## Ambiente canónico do projeto FINAL — 29/10/2026

- **Este é o motor final selecionado pelo proprietário**: o código original do autor `morluto/rea`, tag `rea-agents-6.8.0` e commit fixo `160d821ac9a0310afcb8d1fc427862dd6508add5`, que foi realmente compilado e testado na VPS. O número do pacote é `6.8.0`, mas este é **o checkout independente** e não o motor legado.
- **GitHub fonte canónica**: `martaxi-boss/Engenheira-reversa`, pasta `engenharia-reversa/` e submódulo `engenharia-reversa/original/`. Ler primeiro `engenharia-reversa/project.json` para ver o estado canónico, origem, limites e provas. O legado conserva-se isolado na pasta `rea/`.
- **VPS motor final existente**: `/home/ubuntu/rea-original-upstream-680`; evidências `/home/ubuntu/rea-original-upstream-680-evidence`. **Não voltar a instalar** outro checkout em `/home/ubuntu/engenharia-reversa-novo` nem escolher automaticamente um commit upstream posterior.
- **Ponte de execução já demonstrada**: repositório operacional `martaxi-boss/VPS`, branch `rea/one-skill-bridge-20261023`, workflow `.github/workflows/rea-mcp-transport-20261027.yml`, que executa a CLI **do checkout final** via GitHub Actions e SSH de host verificado. Este repositório serve de ponte operacional e não é a origem do projeto novo. Reutilizar a via que já existe se os conectores autorizados permitirem a ação, sem criar workflows/servidores adicionais nem pedir novos segredos por rotina.
- **Provas históricas do checkout final**: ações `40913611670` (instalação, compilação e capturas), `40915197781` (44 casos de resistência PASS, zero `cleanup_incomplete` nesses cenários), `40944719135` (fornecedores reais e limites). Consultar `references/ambiente_final.md` para os detalhes e provas antes de apresentar resultados.
- **Estado comprovado das dependências e fornecedores**: motor FINAL em `/home/ubuntu/rea-original-upstream-680`, `node_modules` independente em `/home/ubuntu/rea-final-runtime/node_modules` (8/8 PASS, run 40968620168) e 12 distribuicoes copiadas para `/home/ubuntu/rea-final-runtime/vendors` (hashes PASS, run 40969427731). Ghidra, JADX e Unblob deram 11/11 PASS com as copias (run 40969647492); APK pela Skill com os novos caminhos deu 3/3 PASS (run 40970395308); Unblob usa um wrapper de Python independente (run 40970111752). A Skill apontou para os caminhos novos e passou health 4/4 (run 40970285268). **Chromium ainda usa caminho antigo e nao esta funcionalmente certificado. Tambem foram observados processos legados: nao apagar a instalacao antiga sem auditoria de consumidores e ordem de retirada.**
- **Não utilizar o conector antigo `REA_6_8_0` como execução do motor final.** Usar apenas a CLI do checkout final, identificada pelo SHA do commit e caminhos reais. Se não houver possibilidade de executar GitHub Actions/SSH no contexto, distinguir `acesso a registos` de `execução real pendente`.

## Ponte operacional para pedidos reais (GitHub Actions -> SSH -> CLI final)

A Skill pode enviar pedidos de leitura ao motor final pelo conector GitHub instalado. A existencia destas instrucoes nao prova a execucao: **ler os logs exatos de cada pedido**.

- Repositorio de transporte: `martaxi-boss/VPS`, branch `rea/one-skill-bridge-20261023`, ficheiro `rea-linux/skill-requests/current.json`, script `rea-linux/skill-bridge/execute_request.py`, workflow existente `.github/workflows/rea-mcp-transport-20261027.yml`.
- Operacoes permitidas: `health`, `providers`, `inspect_elf`, `apk_demo` (APK publica com hash fixado). Sem comandos shell ou caminhos arbitrarios. Para analisar ficheiros privados do utilizador e preciso primeiro um transporte seguro especifico.
- Primeiro ler `current.json` na branch acima com o conector GitHub `fetch_file`, guardando o SHA do blob. Gerar um identificador unico de 8-80 caracteres `[A-Za-z0-9._-]`.
- Enviar usando GitHub `update_file` na MESMA branch, com a mensagem `skill-request: <request_id>`, o SHA consultado e estas cinco chaves exatas: `schema_version:1`, `project:"engenharia-reversa-final"`, `engine_commit:"160d821ac9a0310afcb8d1fc427862dd6508add5"`, `request_id`, `operation`.
- Obter o SHA do novo commit e procurar a execucao GitHub Actions cujo `head_sha` corresponda exatamente. Ler os jobs com `fetch_workflow_run_jobs`, selecionar `engenharia-reversa-skill`, depois ler os logs via `fetch_workflow_job_logs`.
- Apenas declarar PASS depois de ler `REA_SKILL_BRIDGE_RESULT=<JSON>` e confirmar `request_id`, `status:PASS`, identidade do motor e resultados reais. Se faltar, reportar BLOQUEADO sem inventar sucesso.
- A CLI executa na VPS `/home/ubuntu/rea-original-upstream-680/scripts/rea.mjs` depois de conferir commit, hashes compilados e versao; o conector antigo `REA_6_8_0` nao e utilizado.
- `present:true` na lista de fornecedores so confirma presenca do programa, nao certificacao funcional. `node_modules` esta isolado, mas programas externos e processos legados ainda precisam de certificacao. Nao apagar o legado.
- Este procedimento nao cria novo motor, workflow, servidor, servico ou MCP. Consultar `references/ponte_operacional.md` para exemplos.

## Identidade e separação absoluta

- Tratar esta Skill como **um projeto novo e independente**. Não carregar nem assumir versões de motores, repositórios, branches, servidores, credenciais, integrações, workflows, relatórios ou resultados de projetos anteriores.
- **Nunca importar automaticamente** o estado de outra Skill ou motor de engenharia reversa, mesmo que o nome seja semelhante.
- Trabalhar apenas no projeto e nas fontes **expressamente indicados na tarefa atual**. Na ausência de um repositório, VPS, host ou dispositivo designado, trabalhar localmente sobre o artefacto fornecido ou apresentar um diagnóstico sem tocar em sistemas remotos.
- Não criar ou instalar serviços, conectores, motores, plugins, MCPs, workflows ou ferramentas por rotina. Descobrir e reutilizar apenas ferramentas legitimamente existentes e compatíveis com o ambiente atual. Separar claramente esta Skill (instruções) dos programas externos que poderá usar.

## Entradas suportadas

- Ficheiro local fornecido pelo utilizador (APK, ELF, PE, ZIP, JAR, firmware, biblioteca, registo, captura, documento técnico, etc.).
- Repositório, versão, commit ou endereço expressamente indicado pelo utilizador e acessível através de ferramenta disponível.
- Comparação entre duas versões/artefactos ou diagnóstico de comportamento reproduzível.
- Sistema/dispositivo de teste com autorização explícita e acesso funcional confirmado.

Não pedir perguntas de rotina. Quando faltar uma entrada indispensável, solicitar **apenas** essa entrada e não inventar acessos ou resultados.

## Protocolo de execução

1. **Delimitar o âmbito.** Registar nome do projeto atual, objeto, versão, origem, autorização, objetivos e exclusões. Confirmar que nenhum caminho/serviço de outro projeto entra no plano.
2. **Inventário seguro.** Preferir análise sem execução: tamanho, tipo, SHA-256, cabeçalhos, recursos, estrutura, metadados, dependências. Para um ficheiro, executar `python3 scripts/inspecionar_artefacto.py /caminho/do/ficheiro` se houver um ambiente Python autorizado. O script é só de leitura e não extrai arquivos.
3. **Escolher métodos disponíveis.** Aplicar ferramentas apropriadas **apenas se realmente acessíveis**: leitura binária, desmontagem/descompilação, análise de APK/recursos, inspeção de protocolos, comparação ou pesquisa de código. Não declarar como instalado ou certificado aquilo que apenas aparece num catálogo.
4. **Testes funcionais controlados.** Executar software desconhecido apenas num ambiente isolado e autorizado, com amostras controladas, recursos limitados e plano de limpeza. Não executar binários não confiáveis diretamente em sistemas produtivos. Evitar testes invasivos, instrumentação de terceiros e recolha de segredos.
5. **Provas verificáveis.** Por cada teste, registar comando/ferramenta, entrada e hash, versão, código de saída, dados essenciais, resultado, limitações, tempo e localização das evidências. Distinguir sempre `PASS`, `FAIL`, `BLOQUEADO`, `NÃO TESTADO` e `NÃO APLICÁVEL`. Um workflow concluído com sucesso não demonstra, por si só, que um fornecedor funcionou.
6. **Corrigir de forma mínima.** Primeiro identificar causa e impacto; aplicar alterações apenas no âmbito autorizado, com possibilidade de reversão. Não contornar licenças, autenticação, sandbox, proteções nem políticas de segurança. Alterações materiais ao host exigem decisão do proprietário.
7. **Higienizar e confirmar.** Remover apenas ficheiros temporários **criados e identificados nesta execução**, nunca fazer limpeza global ou apagar provas. Verificar novamente os testes afetados e a ausência de processos temporários abandonados. GitHub/VPS só podem ser alterados se pertencerem explicitamente ao projeto atual.
8. **Entregar.** Mostrar resumo curto, estado por componente, provas reproduzíveis e bloqueios reais. Não inventar contagens, execução remota, acesso root ou certificações.

## Comandos e operações

- Para reconhecer um artefacto sem o executar: `python3 scripts/inspecionar_artefacto.py <ficheiro>`. Para guardar resultado sem substituir ficheiros existentes: `python3 scripts/inspecionar_artefacto.py <ficheiro> --output <novo-relatorio.json>`.
- Os métodos de descompilação ou extração são escolhidos conforme o formato e as ferramentas efetivamente disponíveis. Nunca se deve tratar um APK, um ZIP e um ELF como se fossem o mesmo formato de análise.
- Para auditorias do GitHub, começar pela branch e HEAD atuais e distinguir leituras de alterações. Para a VPS, identificar primeiro o projeto e o utilizador-alvo. **Não usar nenhum host, IP, branch ou segredo legado por inferência.**
- Para análises maiores, seguir `references/metodologia.md`. Para registo e entrega de provas, seguir `references/relatorio.md`.

## Garantias e limites

- Esta Skill não instala um motor de engenharia reversa nem concede acesso à VPS/GitHub; usa apenas ferramentas e permissões realmente disponíveis no contexto da conversa.
- Não assumir que um fornecedor comercial é gratuito ou que um dispositivo está ligado. Não instalar componentes de outro sistema operativo no Linux só para aumentar contagens.
- Executar apenas tarefas legítimas e autorizadas: investigação defensiva, interoperabilidade, análise de software próprio ou disponibilizado com permissão. Recusar ações que contornem proteções ou comprometam terceiros.
- Responder em português de Portugal, com distinção clara entre **confirmado por teste**, **deduzido** e **pendente**.

