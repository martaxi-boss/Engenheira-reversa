# Modelo de relatório técnico

Identificação: projeto atual, artefacto ou repositório, versão/commit, data e âmbito autorizado.

## Estado por componente

| Componente | Estado | Evidência | Próxima decisão |
|---|---|---|---|
| Nome | PASS / FAIL / BLOQUEADO / NÃO TESTADO / NÃO APLICÁVEL | comando ou ficheiro de prova, hash, resultado | ação ou limitação real |

## Prova mínima por ensaio

- Entrada e hash SHA-256 (quando disponível)
- Ferramenta e versão observadas
- Comando ou operação efetivamente executada (sem segredos)
- Código de saída e parte suficiente da resposta para comprovar o resultado
- Localização exata da evidência e data
- Limitações relevantes e impacto
- Processos e temporários criados/eliminados

## Regras de redação

- **PASS** apenas se o comportamento concreto foi demonstrado com resultado verificável.
- **FAIL** significa execução válida com resultado negativo, e não bloqueio de acesso.
- **BLOQUEADO** descreve uma condição externa não resolvida (licença, dependência, segurança, autorização, dispositivo).
- **NÃO TESTADO** é diferente de instalado ou compatível.
- Não inventar links para execuções, identificadores, hashes ou ficheiros.
- Separar sempre correções efetivamente aplicadas de recomendações futuras.
