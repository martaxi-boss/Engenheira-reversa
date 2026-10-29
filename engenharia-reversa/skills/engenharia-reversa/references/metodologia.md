# Metodologia de análise — Projeto isolado

## Primeiro contacto

Identificar o objetivo, o material de entrada e a sua origem. A ausência de ferramentas de análise binária não justifica inventar provas nem instalar programas sem âmbito.

## Escolha por tipo de entrada

| Tipo | Primeiras verificações | Análise complementar condicionada |
|---|---|---|
| APK/JAR | ZIP, manifesto/recursos, hash, assinaturas disponíveis | análise DEX e classes usando ferramenta autorizada |
| ELF/PE/Mach-O | cabeçalhos, arquitetura, segmentos, imports/exports e strings | desmontagem, símbolos e depuração isolada |
| Firmware | contentores, compressão, partições e assinaturas | extração limitada e análise de sistema de ficheiros |
| Web/JavaScript | recursos públicos ou fornecidos, fontes e dependências | execução num browser isolado, respeitando origem/autorização |
| Repositório | revisão, branch, ficheiros, dependências, configurações | testes unitários e de integração no ambiente delimitado |
| Logs/capturas | timestamps, integridade, formato e escopo | reprodução de falha sem divulgar dados privados |

## Segurança operacional

- O script de inventário incluído nunca executa nem extrai ficheiros recebidos.
- Para análise dinâmica, restringir rede/permissões e usar alvos próprios ou ambientes de laboratório. Separar observação de modificação.
- Evitar guardar tokens, senhas e dados pessoais nos relatórios. Não carregar amostras privadas para serviços públicos sem autorização.
- Antes de limpeza de GitHub/VPS, listar os recursos exatos pertencentes ao projeto atual; preservar evidências e garantir reversibilidade.
- Não considerar uma conclusão de ferramenta como certeza absoluta; correlacionar com dados independentes quando relevante.

## Etapas de verificação de uma correção

1. Observar a falha com evidência original.
2. Determinar a causa sem adivinhar.
3. Definir alteração mínima e respetivo âmbito.
4. Aplicar em ambiente de teste.
5. Repetir o cenário original e confirmar ausência de regressão.
6. Higienizar apenas recursos próprios e guardar o estado final.
