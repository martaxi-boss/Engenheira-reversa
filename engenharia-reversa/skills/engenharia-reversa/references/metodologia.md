# Metodologia simples da Engenharia Reversa FINAL

1. O utilizador ativa a Skill e define a tarefa; não é preciso decidir qual o motor a usar.
2. O agente consulta o MCP original do REA quando necessita conhecer as ferramentas e os seus contratos.
3. O agente chama as ferramentas adequadas com os argumentos suportados, usando `mcp_requests` através do GitHub Actions/SSH existente.
4. O REA original executa as operações com os seus fornecedores e dependências, sem lógica duplicada no transporte.
5. O agente interpreta as evidências devolvidas e continua a análise; chamadas dependentes podem ir na mesma sessão MCP.
6. Comunicar os IDs das execuções, os resultados reais e os limites observados. Não atribuir ao motor tarefas que ele não executou.
