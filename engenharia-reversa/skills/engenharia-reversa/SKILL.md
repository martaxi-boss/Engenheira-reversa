---
name: engenharia-reversa
description: Aceder ao motor original Engenharia Reversa FINAL instalado na VPS quando o utilizador invoca a Skill. Usar o MCP original a partir do agente do chat por GitHub Actions e SSH, sem duplicar ferramentas, fornecedores ou regras de análise na ligação.
---

# Engenharia Reversa FINAL — motor original na VPS

**Identidade:** Engenharia Reversa FINAL — motor original do autor instalado na VPS. A inteligência artificial é a do chat escolhido pelo utilizador; não existe outra IA do projeto instalada na VPS. Quando o utilizador ativa esta Skill, quer **utilizar efetivamente o motor REA**, não um substituto nem um diagnóstico genérico.

## Motor preservado

- Autor: `morluto/rea`, versão original do pacote `rea-agents 6.8.0`, commit fixado `160d821ac9a0310afcb8d1fc427862dd6508add5`.
- Instalação Linux: `/home/ubuntu/rea-original-upstream-680`.
- Dependências e fornecedores independentes: `/home/ubuntu/rea-final-runtime/{node_modules,vendors,optional}`.
- **Não alterar nem duplicar o motor original, os fornecedores ou as dependências.** A instalação antiga em `/opt/rea-reversa` foi retirada.

## Ligação única, já existente

ChatGPT/agente → Skill → GitHub (`martaxi-boss/VPS`, ramo `rea/one-skill-bridge-20261023`) → workflow `.github/workflows/rea-mcp-transport-20261027.yml` → SSH autenticado → **REA MCP original em stdio** → resultados no mesmo chat.

O ficheiro `rea-linux/skill-bridge/execute_request.py` é **apenas um transporte de mensagens MCP**. Não tem catálogo de ferramentas próprio, lista fixa de operações, seleção de fornecedores nem implementação de análises. O REA original valida e executa as chamadas MCP. Não criar outra ponte, motor, servidor, MCP, workflow nem coordenador.

## Utilização real

1. O utilizador ativa a Skill e dá o pedido. O agente de IA do chat conduz a tarefa com o **catálogo real de ferramentas disponibilizado pelo REA**, em vez de tentar reconhecer qual o motor a utilizar.
2. Ler `rea-linux/skill-requests/current.json` na branch indicada e guardar o SHA do ficheiro. Substituir pelo pedido com `request_id` novo e uma lista `mcp_requests` de chamadas **MCP nativas**, por exemplo:

```json
{
  "request_id": "rea-exemplo-20261030-001",
  "mcp_requests": [
    {"method": "tools/list", "params": {}},
    {"method": "tools/call", "params": {"name": "inspect_analysis_settings", "arguments": {}}}
  ]
}
```

3. Utilizar o conector GitHub `update_file` na mesma branch, com a mensagem de commit `skill-request: <request_id>`. Encontrar o run GitHub Actions pelo **novo commit SHA**, não por aproximação temporal.
4. Ler o job `engenharia-reversa-skill` e o resultado `REA_SKILL_BRIDGE_RESULT=`. O campo `responses` contém as respostas originais do protocolo MCP. Em respostas grandes, concatenar as linhas `REA_MCP_RESULT_PART=N/T:...` pela ordem N, fazer `JSON.parse` do texto reunido e comparar com o `request_id` e o estado da execução. A fragmentação é apenas para não cortar resultados nos logs.
5. Interpretar o resultado e, se a investigação exigir outras ferramentas, emitir novas chamadas MCP. **Ferramentas que partilham sessão devem constar do mesmo `mcp_requests`** (por exemplo `open_binary` e depois `inspect_artifact`). Cada workflow abre uma sessão MCP temporária no motor instalado na VPS.
6. Apresentar o ID do run, as ferramentas realmente chamadas, os resultados e as limitações observadas. Não confundir `tools/list` com certificação funcional das ferramentas nem `health` com auditoria de um projeto.

**Não criar listas artificiais de ferramentas, limites de cinco chamadas, seletores de fornecedores ou verificações duplicadas de contratos.** O motor REA já publica os seus contratos MCP, escolhe fornecedores quando a operação o suporta e executa com as dependências existentes.

Respeitar o objetivo e o âmbito autorizado pelo utilizador. Alterações destrutivas ou operações que afetem terceiros exigem autorização adequada do utilizador, mas não introduzir bloqueios técnicos adicionais na ligação. Preservar a autenticação SSH existente e não revelar credenciais.

## Provas reais da ligação simples

- [41035333062](https://github.com/martaxi-boss/VPS/actions/runs/41035333062): chamada MCP direta `tools/call` executada com sucesso na VPS.
- [41035502436](https://github.com/martaxi-boss/VPS/actions/runs/41035502436): mesma sessão com `tools/list` (229 ferramentas) e `tools/call`, ambas com sucesso; a resposta integral foi recuperada dos logs.

Para pormenores do transporte e dos resultados, ler `references/ponte_operacional.md`. Para histórico da instalação, ler `references/ambiente_final.md`.
