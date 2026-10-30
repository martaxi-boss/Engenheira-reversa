# Engenharia Reversa — projeto FINAL (29 de outubro de 2026)

**Este é o motor FINAL escolhido pelo proprietário.** Foi mantido o checkout original efetivamente testado na VPS. Não criar novo motor, novo workflow, MCP ou coordenador.

## Identidade e repositórios

- **Motor na VPS Ubuntu:** `/home/ubuntu/rea-original-upstream-680`
- **Código original do autor:** `morluto/rea`, commit fixo `160d821ac9a0310afcb8d1fc427862dd6508add5`, tag `rea-agents-6.8.0`.
- **Versão do pacote:** `6.8.0`. O projeto final usa a instalação separada e comprovada; este número não corresponde a um motor novo inventado.
- **Fonte canónica no GitHub:** `martaxi-boss/Engenheira-reversa`, pasta `engenharia-reversa/`; submódulo `engenharia-reversa/original` fixado no commit acima.
- **Transporte operacional existente:** `martaxi-boss/VPS`, branch `rea/one-skill-bridge-20261023`, workflow `.github/workflows/rea-mcp-transport-20261027.yml`; GitHub Actions → SSH de host fixado → CLI do motor final.
- **Evidências locais:** `/home/ubuntu/rea-original-upstream-680-evidence`.
- **Legado retirado em 30/10/2026:** `/opt/rea-reversa` eliminado da VPS; `rea/` e `certifications/` retirados da árvore Git atual, mantendo o histórico.

## Estrutura de dependências reorganizada na VPS

| Elemento | Caminho | Estado verificado |
| --- | --- | --- |
| Motor final (código original) | `/home/ubuntu/rea-original-upstream-680` | PASS |
| Módulos Node.js próprios (~866 MiB) | `/home/ubuntu/rea-final-runtime/node_modules` | **Ativos; 8/8 testes PASS** |
| Cópias independentes de 12 fornecedores (~2,19 GiB) | `/home/ubuntu/rea-final-runtime/vendors` | **Cópias ativas na ligação da Skill; 11 testes funcionais PASS em fornecedores selecionados** |
| Provas e inventários | `/home/ubuntu/rea-original-upstream-680-evidence/isolation-20261029` | Preservados |
| Instalação anterior | `/opt/rea-reversa` | Eliminada após confirmação de autonomia; motor final testado novamente |

As cópias incluem Node 24, JDK 21, Ghidra, JADX, Unblob, Binwalk, Rizin, Kuna, Wakaru, Mitmproxy, Cutter e WABT. A Skill já usa os novos caminhos; isto não certifica individualmente todas as funções dos doze programas. O Chromium foi copiado para a pasta privada final e teve versão verificada; a sessão de navegador continua sem certificação por limitações de sandbox/AppArmor. O Hopper comercial foi excluído do inventário ativo do projeto final. A presença ou cópia de um programa **não equivale** a todas as suas funções estarem certificadas.

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

## Retirada concluída da instalação antiga (30/10/2026)

O proprietário autorizou a retirada. Os serviços `rea-reversa-mcp.service` e `rea-mcp-oauth.service` foram desativados e parados. A VPS eliminou `/opt/rea-reversa` (incluindo `rea`, `providers`, `tools`, `oauth-auth` e os resíduos finais), com confirmação de `LEGADO ELIMINADO` e `MOTOR FINAL: OK` e cerca de 29 GB livres no disco, demonstrada no terminal do proprietário.

No GitHub, as árvores antigas `rea/` e `certifications/` e cinco referências de submódulos antigos foram retiradas da versão atual. O submódulo `engenharia-reversa/original`, a Skill, o código e as provas do motor final foram preservados. O histórico Git anterior não foi reescrito e os registos anteriores podem ser consultados por commit.

A confirmação de funcionamento pós-retirada é um teste real da CLI `providers --json` no motor final, não certificação de todas as ferramentas e interfaces opcionais. Consultar [RETIRADA_LEGADO.md](RETIRADA_LEGADO.md).


## Revalidação real após remoção (30/10/2026)

- [Health GitHub Actions #40980208602](https://github.com/martaxi-boss/VPS/actions/runs/40980208602): motor original validado por commit e hashes, `ISOLATED_FINAL_RUNTIME`, 4/4 operações PASS, 25 fornecedores inventariados e 0 referências ativas ao legado.
- [Separação rigorosa #40980322799](https://github.com/martaxi-boss/VPS/actions/runs/40980322799): 9 252 itens do checkout e 64 713 do runtime verificados, 290 links simbólicos examinados, 0 links ou fornecedores ativos a apontar para o legado, 0 lançadores antigos nos ficheiros examinados.
- [Limpeza do GitHub/VPS #40980084601](https://github.com/martaxi-boss/VPS/actions/runs/40980084601): ponte existente validada após retirada dos scripts do legado na branch operacional por PR #310.
- **Limite:** a Skill já foi corrigida no repositório, mas a release atualmente instalada no ChatGPT ainda contém instruções anteriores à retirada. A atualização da release requer identificar o plugin original; não confundir fonte GitHub atualizada com release do plugin efetivamente instalada.

## Verificação, documentação e Skill

- `project.json` guarda identidade, estado real e IDs das provas.
- `scripts/vps_verify_existing.py` faz verificação de leitura do checkout, sem instalação ou limpeza.
- `skills/engenharia-reversa/SKILL.md` define a execução por GitHub Actions na VPS.
- `.github/workflows/engenharia-reversa-novo.yml` certifica a estrutura canónica no GitHub, sem criar instalações na VPS.

O motor final continua único e independente; a retirada do legado foi expressamente autorizada e concluída.

## Auditoria integral comparativa com o autor (29/10/2026)

Foi executada auditoria read-only na VPS [40971914250](https://github.com/martaxi-boss/VPS/actions/runs/40971914250), complementada por diagnósticos [40972191490](https://github.com/martaxi-boss/VPS/actions/runs/40972191490), comparando o motor final com **o mesmo commit original do autor**, não com a instalação antiga. Resultado: **42/42 dependências npm obrigatórias, 1/1 Frida opcional, 27/27 de desenvolvimento e 26/26 programas no inventário disponíveis**. Ghidra/JADX/Kuna PASS; Hopper/IDA opcionais pendentes. O relatório identifica ferramentas gratuitas opcionais não encontradas no PATH e as não aplicáveis a Linux. Ver [AUDITORIA_COMPARATIVA_ORIGINAL_20261029.md](AUDITORIA_COMPARATIVA_ORIGINAL_20261029.md). Não houve instalações nem remoções.

## Separação rigorosa do motor antigo — verificada

Os componentes específicos do motor final têm agora cópias próprias, sem qualquer caminho ativo para a instalação 6.8 antiga. Foram analisados 9 252 itens no checkout e 64 713 no runtime, incluindo 290 symlinks (0 para o legado): [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346). A Skill passou health 4/4 e APK 3/3 após a migração, com regra de bloqueio de regressão no bridge. Ver [SEPARACAO_ABSOLUTA_20261029.md](SEPARACAO_ABSOLUTA_20261029.md). Após identificação e paragem dos dois serviços antigos, a instalação antiga foi retirada; a verificação posterior do motor final passou.
