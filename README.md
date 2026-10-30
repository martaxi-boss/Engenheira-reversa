# Engenharia Reversa — motor FINAL independente

Este repositório mantém o projeto final em [`engenharia-reversa/`](engenharia-reversa/README.md), com o **código original do autor** [`morluto/rea`](https://github.com/morluto/rea) fixado no commit `160d821ac9a0310afcb8d1fc427862dd6508add5`.

O pacote original declara versão `6.8.0`, mas **a instalação final não é a antiga instalação REA removida**. A identificação deve ser feita pelo caminho e pelo commit, não apenas pelo número do pacote.

## VPS e funcionamento

- Motor final: `/home/ubuntu/rea-original-upstream-680`
- Dependências e fornecedores exclusivos: `/home/ubuntu/rea-final-runtime`
- Ligação operacional já existente: [`martaxi-boss/VPS`](https://github.com/martaxi-boss/VPS), branch `rea/one-skill-bridge-20261023`, GitHub Actions → SSH → CLI final.
- Health real [40974869693](https://github.com/martaxi-boss/VPS/actions/runs/40974869693), análise Android [40974717355](https://github.com/martaxi-boss/VPS/actions/runs/40974717355), isolamento [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346).

## Retirada do motor antigo — 30/10/2026

A VPS deixou de conter `/opt/rea-reversa`: os serviços antigos foram parados e desativados, a pasta foi eliminada e a CLI final voltou a funcionar (`providers --json`). O proprietário confirmou `LEGADO ELIMINADO` e `MOTOR FINAL: OK` no terminal, com cerca de 29 GB livres.

Da árvore atual do GitHub foram retiradas `rea/`, `certifications/` e as referências a cinco submódulos do projeto antigo. O submódulo `engenharia-reversa/original` foi preservado. Os commits históricos não foram reescritos e podem ser consultados, mas a eliminação da árvore atual não garante diminuição imediata do armazenamento remoto.

Ver o [registo de retirada](engenharia-reversa/RETIRADA_LEGADO.md), a [auditoria comparativa original](engenharia-reversa/AUDITORIA_COMPARATIVA_ORIGINAL_20261029.md) e a [Skill versionada](engenharia-reversa/skills/engenharia-reversa/SKILL.md).

**Não reinstalar o REA legado, não reintroduzir dependências antigas e não confundir a pasta `rea/` removida com o submódulo `engenharia-reversa/original` preservado.**
