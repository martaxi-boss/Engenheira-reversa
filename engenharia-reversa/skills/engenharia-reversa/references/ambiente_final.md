# Ambiente final e historico comprovado — 29/10/2026

## Identidade

- Fonte oficial: `https://github.com/morluto/rea.git` no commit imutavel `160d821ac9a0310afcb8d1fc427862dd6508add5`, tag `rea-agents-6.8.0`.
- Codigo novo: `martaxi-boss/Engenheira-reversa`, pasta `engenharia-reversa/original/` no commit acima. `engenharia-reversa/project.json` e o estado canónico atualizado.
- Instalacao real testada na VPS Ubuntu: `/home/ubuntu/rea-original-upstream-680`.
- Evidencias: `/home/ubuntu/rea-original-upstream-680-evidence`.
- Ponte existente: `martaxi-boss/VPS`, branch `rea/one-skill-bridge-20261023`, workflow `.github/workflows/rea-mcp-transport-20261027.yml`, GitHub Actions/SSH -> CLI do checkout novo.

## Provas de 29/10

- https://github.com/martaxi-boss/VPS/actions/runs/40913611670: fonte original, compilacao positiva e capturas de subprocessos em ambiente real.
- https://github.com/martaxi-boss/VPS/actions/runs/40915197781: 44 cenarios de resistencia aprovados, nenhum `cleanup_incomplete` nesses casos.
- https://github.com/martaxi-boss/VPS/actions/runs/40944719135: Binwalk 3.1 PASS em inspecao real; Frida descoberta sem alvo; Cutter presente sem bridge GUI ativa; Chromium presente mas sem sessao iniciada; capturas complementares PASS.

Os testes acima nao provam que todas as ferramentas e fornecedores foram certificados sem excecoes. Nao repetir ensaios validos sem alteracao material do ambiente.

## Dependencias e regra de eliminacao

- Ultimo estado conhecido: a pasta `node_modules` do motor final e um symlink para o antigo `/opt/rea-reversa/rea/node_modules`; alguns binarios externos estao sob `/opt/rea-reversa/providers`.
- Isso torna a independencia completa **pendente**, mesmo que o motor final tenha passado os testes da tarde. Antes de eliminar o legado, obter dependencias e fornecedores autonomos, verificar o ambiente atual da VPS e repetir os testes afetados.
- Nao eliminar, relocalizar, parar servicos ou limpar ficheiros do projeto antigo sem nova ordem explicita do proprietario, apos certificacao de autonomia.

## Uso na Skill

1. Consultar GitHub `engenharia-reversa/project.json` do `main`, verificando estado e revisionamento.
2. Ler os logs acima para separar resultados da tarde de verificacoes atuais.
3. Para observacoes reais de VPS, usar apenas o caminho operacional GitHub Actions/SSH ja comprovado, se houver permissao e ferramenta. Se o conector nao oferecer despacho/execucao, registrar `BLOQUEADO`, sem fingir que executar uma leitura de GitHub e o mesmo que executar SSH.
4. Identificar em cada relatorio qual motor (por commit, caminho e ferramenta) foi realmente utilizado.
