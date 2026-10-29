# Engenharia Reversa — motor final de 29 de outubro de 2026

**Este é o projeto final escolhido pelo proprietário.** Não instalar outro motor em paralelo, nem substituir os trabalhos efetuados à tarde.

## Identidade do motor final testado

- Fonte oficial: `https://github.com/morluto/rea.git`.
- Commit efetivamente testado no Ubuntu: `160d821ac9a0310afcb8d1fc427862dd6508add5` (tag do autor `rea-agents-6.8.0`).
- A versão do pacote continua `6.8.0`; a instalação é independente da instalação legada.
- Instalação real na VPS: `/home/ubuntu/rea-original-upstream-680`.
- Evidências e registos na VPS: `/home/ubuntu/rea-original-upstream-680-evidence`.
- Arquivo de código deste novo projeto no GitHub: `engenharia-reversa/original` (submódulo diretamente ao autor no commit exato).
- Projeto legado, preservado: pasta `rea/` no mesmo repositório e instalação `/opt/rea-reversa/rea` na VPS.

## Resultados já testados na VPS

- [Run 40913611670](https://github.com/martaxi-boss/VPS/actions/runs/40913611670): fonte oficial, dependências verificadas, compilação e seis capturas reais com resultado positivo.
- [Run 40915197781](https://github.com/martaxi-boss/VPS/actions/runs/40915197781): 44/44 ensaios controlados, 0 falhas e 0 ocorrências de `cleanup_incomplete` nos cenários observados.
- [Run 40944719135](https://github.com/martaxi-boss/VPS/actions/runs/40944719135): Binwalk 3.1 com inspeção real PASS; Frida descoberta sem prova em alvo; Cutter instalado sem bridge GUI ativa; Chromium instalado sem sessão iniciada.

Estes são resultados limitados aos cenários comprovados. Não afirmar que todas as 229 ferramentas ou todos os fornecedores funcionam.

## Via de execução que já funcionou

A operação real usou GitHub Actions do repositório `martaxi-boss/VPS`, ramo `rea/one-skill-bridge-20261023`, workflow `.github/workflows/rea-mcp-transport-20261027.yml`, via SSH com identidade de host validada, executando o CLI na instalação `/home/ubuntu/rea-original-upstream-680`. **O fluxo operacional existe; não criar ligações alternativas por rotina.** A cópia do código e a Skill do projeto final pertencem à pasta `engenharia-reversa/` deste repositório.

## Bloqueio a resolver antes de eliminar o antigo

Na última verificação, a instalação final reutilizava `node_modules` por ligação simbólica para `/opt/rea-reversa/rea/node_modules`. Alguns fornecedores também estavam em `/opt/rea-reversa/providers`. **O motor final foi testado, mas ainda não é totalmente independente do legado.** Migrar/verificar as dependências e fornecedores necessários, sem apagar nem modificar o legado, e repetir apenas os testes afetados antes de autorizar eliminação.

## Skill versionada

A fonte da Skill associada a este projeto está em [`skills/engenharia-reversa/SKILL.md`](skills/engenharia-reversa/SKILL.md). O pacote de atualização da Skill deve refletir estes ficheiros, mas a inclusão no GitHub **não prova** atualização da instalação no ChatGPT nem uma chamada efetiva ao motor na VPS.

## Estado e verificação

- `project.json` fixa a identidade, ambiente real, ligação operacional, provas e limites.
- `scripts/vps_verify_existing.py` observa o motor existente (não instala, não modifica e não remove).
- `.github/workflows/engenharia-reversa-novo.yml` valida o código GitHub sem instalar duplicados na VPS.
- A Skill `engenharia-reversa` deve ser atualizada para apontar a este motor e esta ligação; a comunicação real da Skill com o motor continua por provar ponta-a-ponta.

**A eliminação de `rea/` e dos componentes legados exige ordem expressa posterior do proprietário.**
