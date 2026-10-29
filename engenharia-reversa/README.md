# Engenharia Reversa — projeto FINAL (29 de outubro de 2026)

**Este é o motor FINAL escolhido pelo proprietário.** Foi mantido o checkout original efetivamente testado na VPS. Não criar novo motor, novo workflow, MCP ou coordenador.

## Identidade e repositórios

- **Motor na VPS Ubuntu:** `/home/ubuntu/rea-original-upstream-680`
- **Código original do autor:** `morluto/rea`, commit fixo `160d821ac9a0310afcb8d1fc427862dd6508add5`, tag `rea-agents-6.8.0`.
- **Versão do pacote:** `6.8.0`. O projeto final usa a instalação separada e comprovada; este número não corresponde a um motor novo inventado.
- **Fonte canónica no GitHub:** `martaxi-boss/Engenheira-reversa`, pasta `engenharia-reversa/`; submódulo `engenharia-reversa/original` fixado no commit acima.
- **Transporte operacional existente:** `martaxi-boss/VPS`, branch `rea/one-skill-bridge-20261023`, workflow `.github/workflows/rea-mcp-transport-20261027.yml`; GitHub Actions → SSH de host fixado → CLI do motor final.
- **Evidências locais:** `/home/ubuntu/rea-original-upstream-680-evidence`.
- **Legado preservado:** `rea/` no GitHub e `/opt/rea-reversa/rea` na VPS.

## Estrutura de dependências reorganizada na VPS

| Elemento | Caminho | Estado verificado |
| --- | --- | --- |
| Motor final (código original) | `/home/ubuntu/rea-original-upstream-680` | PASS |
| Módulos Node.js próprios (~866 MiB) | `/home/ubuntu/rea-final-runtime/node_modules` | **Ativos; 8/8 testes PASS** |
| Cópias independentes de 12 fornecedores (~2,19 GiB) | `/home/ubuntu/rea-final-runtime/vendors` | **Cópias ativas na ligação da Skill; 11 testes funcionais PASS em fornecedores selecionados** |
| Provas e inventários | `/home/ubuntu/rea-original-upstream-680-evidence/isolation-20261029` | Preservados |
| Instalação anterior | `/opt/rea-reversa/rea` | Preservada; sem remoção |

As cópias incluem Node 24, JDK 21, Ghidra, JADX, Unblob, Binwalk, Rizin, Kuna, Wakaru, Mitmproxy, Cutter e WABT. A Skill já usa os novos caminhos; isto não certifica individualmente todas as funções dos doze programas. Foram excluídos Chromium (sandbox/AppArmor bloqueado) e Hopper (build/licença não certificada). A presença ou cópia de um programa **não equivale** a todas as suas funções estarem certificadas.

## Evidências reais (GitHub Actions → VPS)

- [40915197781](https://github.com/martaxi-boss/VPS/actions/runs/40915197781): 44/44 testes de resistência, sem `cleanup_incomplete` nos cenários ensaiados.
- [40965936183](https://github.com/martaxi-boss/VPS/actions/runs/40965936183): pedido originado na Skill instalada, motor final e quatro operações reais PASS.
- [40968408461](https://github.com/martaxi-boss/VPS/actions/runs/40968408461): cópia independente dos módulos Node com verificações de integridade.
- [40968620168](https://github.com/martaxi-boss/VPS/actions/runs/40968620168): troca da ligação do `node_modules` para a cópia independente e **8/8 testes reais PASS**, incluindo três análises Android.
- [40968899758](https://github.com/martaxi-boss/VPS/actions/runs/40968899758): ensaios funcionais Ghidra, JADX, Unblob e limpeza de processos depois da troca.
- [40969427731](https://github.com/martaxi-boss/VPS/actions/runs/40969427731): **12 fornecedores copiados e 12 ficheiros de entrada comparados por SHA-256**.
- [40969647492](https://github.com/martaxi-boss/VPS/actions/runs/40969647492): **11/11** testes funcionais Ghidra, JADX, Unblob, limpeza; detetada e corrigida depois a referência interna antiga do launcher Unblob.
- [40970111752](https://github.com/martaxi-boss/VPS/actions/runs/40970111752): Unblob testado com Python da nova pasta por wrapper próprio, extração real e hashes PASS.
- [40970285268](https://github.com/martaxi-boss/VPS/actions/runs/40970285268): **Skill → GitHub → SSH → motor final**, agora com caminhos do runtime próprio, saúde 4/4 PASS; 26 componentes presentes, apenas Chromium ainda referenciado na pasta antiga.
- [40970395308](https://github.com/martaxi-boss/VPS/actions/runs/40970395308): **Skill analisa APK com os novos caminhos, 3/3 PASS**, sem `cleanup_incomplete`.

Estes resultados não significam que todas as 229 ferramentas do catálogo tenham sido certificadas neste motor.

## O que falta para remover o legado

1. **Confirmar os fornecedores opcionais ainda não certificados e quaisquer referências internas restantes**. Chromium continua na pasta antiga e não tem sessão funcional certificada; Hopper continua com limitações de versão/licença.
2. Validar os serviços/processos que continuam a utilizar a instalação antiga (na auditoria anterior foram encontrados dois), antes de interromper ou remover qualquer um.
3. Repetir os testes afetados, confirmar a Skill, preservar os dados e obter uma ordem separada de remoção.
4. Para redução de espaço no GitHub, lembrar que apagar ficheiros do HEAD não remove automaticamente os objetos do histórico Git; nunca reescrever histórico ou fazer force-push sem aprovação específica.

**Não apagar já `rea/`, `/opt/rea-reversa/rea`, os fornecedores antigos nem as evidências.** Consultar [RETIRADA_LEGADO.md](RETIRADA_LEGADO.md) para as condições verificáveis.

## Verificação, documentação e Skill

- `project.json` guarda identidade, estado real e IDs das provas.
- `scripts/vps_verify_existing.py` faz verificação de leitura do checkout, sem instalação ou limpeza.
- `skills/engenharia-reversa/SKILL.md` define a execução por GitHub Actions na VPS.
- `.github/workflows/engenharia-reversa-novo.yml` certifica a estrutura canónica no GitHub, sem criar instalações na VPS.

O motor final é único; as provas são rastreáveis e cada migração é reversível até à eliminação expressamente autorizada do legado.
