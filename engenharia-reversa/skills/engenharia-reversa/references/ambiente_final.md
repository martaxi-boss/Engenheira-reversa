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

## Dependencias proprias e retirada concluida em 30/10/2026

- A versao de codigo que permanece e a **original do autor**, `morluto/rea` no commit `160d821ac9a0310afcb8d1fc427862dd6508add5`, pacote oficial `6.8.0`. A versao do pacote nao deve ser renomeada por causa da retirada da instalacao antiga.
- `node_modules` do motor final agora liga exclusivamente a `/home/ubuntu/rea-final-runtime/node_modules`; demonstrado em [40968620168](https://github.com/martaxi-boss/VPS/actions/runs/40968620168).
- Os fornecedores ativos ficam na pasta independente `/home/ubuntu/rea-final-runtime/vendors`, e os opcionais no runtime privado, validados nos ensaios [40969647492](https://github.com/martaxi-boss/VPS/actions/runs/40969647492), [40974350944](https://github.com/martaxi-boss/VPS/actions/runs/40974350944) e [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346). Isto nao certifica automaticamente todos os fornecedores.
- **Legado retirado:** os dois servicos antigos foram parados e desativados; a pasta `/opt/rea-reversa` foi eliminada pelo proprietario em 30/10/2026. O comando de teste de fornecedores do motor final passou **apos** a retirada e o terminal mostrou `LEGADO ELIMINADO` e `MOTOR FINAL: OK`.
- No GitHub final, `rea/`, `certifications/` e cinco submodulos antigos foram removidos do HEAD pelo PR #10. Os commits antigos mantem-se no historico, sem reescrita.
- **Nao** reinstalar dependencias, fornecedores, processos ou servicos antigos. Manter isolado o motor final, sem modificar o codigo do autor.

## Uso na Skill

1. Consultar GitHub `engenharia-reversa/project.json` do `main`, verificando estado e revisionamento.
2. Ler os logs acima para separar resultados da tarde de verificacoes atuais.
3. Para observacoes reais de VPS, usar apenas o caminho operacional GitHub Actions/SSH ja comprovado, se houver permissao e ferramenta. Se o conector nao oferecer despacho/execucao, registrar `BLOQUEADO`, sem fingir que executar uma leitura de GitHub e o mesmo que executar SSH.
4. Identificar em cada relatorio qual motor (por commit, caminho e ferramenta) foi realmente utilizado.
