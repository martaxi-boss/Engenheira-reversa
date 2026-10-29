# Porta de retirada do motor antigo — apenas plano, sem eliminação

**Motor a preservar:** `/home/ubuntu/rea-original-upstream-680`, commit do autor `160d821ac9a0310afcb8d1fc427862dd6508add5`.

**Instalação antiga a avaliar futuramente:** `/opt/rea-reversa/rea`; pastas `/opt/rea-reversa/tools` e `/opt/rea-reversa/providers`; código legado `rea/` e submódulos correspondentes no GitHub. **Não executar remoções automáticas.**

## Portas comprovadas

- [x] Motor final compilado e identificado por commit/hashes.
- [x] `node_modules` independente em `/home/ubuntu/rea-final-runtime/node_modules`; 8 testes PASS — [40968620168](https://github.com/martaxi-boss/VPS/actions/runs/40968620168).
- [x] 12 fornecedores copiados para `/home/ubuntu/rea-final-runtime/vendors`, entradas comparadas por SHA-256 — [40969427731](https://github.com/martaxi-boss/VPS/actions/runs/40969427731).
- [x] Ghidra, JADX e Unblob funcionais com as cópias — [40969647492](https://github.com/martaxi-boss/VPS/actions/runs/40969647492).
- [x] Unblob a usar Python da nova cópia, sem invocar o antigo launcher — [40970111752](https://github.com/martaxi-boss/VPS/actions/runs/40970111752).
- [x] Skill → GitHub Actions → SSH → motor final a utilizar caminhos novos, 4/4 operações PASS — [40970285268](https://github.com/martaxi-boss/VPS/actions/runs/40970285268).
- [x] APK pública analisada pela Skill com fornecedores copiados, 3/3 operações PASS — [40970395308](https://github.com/martaxi-boss/VPS/actions/runs/40970395308).

## Portas que impedem eliminar o antigo já

- [ ] **Consumidores ativos:** a auditoria [40968060294](https://github.com/martaxi-boss/VPS/actions/runs/40968060294) encontrou dois processos associados a caminhos antigos (um Node e um Python). Confirmar que serviço os utiliza, se pertence a outro projeto e que substituição é adequada. Não parar processos de terceiros.
- [x] **Chromium sem partilha:** cópia própria em `/home/ubuntu/rea-final-runtime/vendors/providers/chromium-playwright-1.58.2` (run 40974091601). A sessão de navegador **não** está certificada devido ao sandbox; não contornar AppArmor.
- [ ] **Hopper:** pacote externo existente, versão/build não certificado para o motor, sem licença paga. Não adicionar aos fornecedores certificados por simples presença.
- [x] **Referências internas usadas pela Skill:** auditados 9 252 itens do checkout e 64 713 do runtime, incluindo 290 symlinks: 0 referências de execução e 0 links para o motor antigo no escopo [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346). Não confundir isto com certificação de todas as 229 ferramentas.
- [ ] **Verificação de serviço pós-retirada:** plano de rollback, prova de saúde e ensaios com entradas controladas após migração dos consumidores.
- [ ] **Autorização separada de remoção:** somente depois de todas as portas acima estarem resolvidas, identificar caminhos exatos autorizados, estimativa de espaço libertado e plano de reversão.

## GitHub

O projeto final tem o seu diretório `engenharia-reversa/` e runtime exclusivo na VPS, com o original fixado como submódulo. O antigo está em `rea/` (árvore Git e respetivos submódulos), `certifications/` e histórico. **Não apagar ainda**. Quando for expressamente aprovado, preparar um PR que remova apenas os caminhos legados e as secções legadas de `.gitmodules`, preservando o submódulo final, código e evidências essenciais. Remover ficheiros do HEAD diminui o checkout, mas não elimina automaticamente o histórico Git nem garante uma redução igual do armazenamento remoto; não executar reescrita de histórico/force push por rotina.

## Regras

Não criar outro motor, não usar Codex, não instalar MCP adicional, não mexer noutros projetos. A ligação operacional é o workflow SSH já existente em `martaxi-boss/VPS`; GitHub é fonte documental, não um substituto do teste real.

## Medição final de espaço e consumidores (auditoria read-only 29/10)

[GitHub Actions 40971066042](https://github.com/martaxi-boss/VPS/actions/runs/40971066042) comprovou:

| Pasta | Espaço ocupado aproximado |
| --- | ---: |
| `/opt/rea-reversa/rea` (motor antigo **incluindo** os módulos) | 1,01 GiB |
| `/opt/rea-reversa/rea/node_modules` (subpasta acima, **não somar novamente**) | 0,85 GiB |
| `/opt/rea-reversa/providers` (instalações externas antigas) | 3,00 GiB |
| `/opt/rea-reversa/tools` (programas externos antigos) | 1,24 GiB |
| `/home/ubuntu/rea-final-runtime` (estrutura final, já copiada e ativa) | 3,04 GiB |
| VPS — espaço livre após cópias | 23,71 GiB |

**Não equivale a espaço recuperável imediatamente**: pode haver conteúdo partilhado com outros serviços, caches protegidos, fornecedores opcionais ainda não migrados e ficheiros necessários a provas.

Foram observados **dois processos** que referenciam caminhos da árvore antiga: um processo Node com referência direta ao **motor legado**, e um processo Python com referência a caminhos antigos que precisam de ser identificados. Nenhum foi parado ou alterado. O motor final mantém o estado `ISOLATED_FINAL_RUNTIME` no diagnóstico.

**Próxima condição obrigatória:** identificar os serviços associados aos dois processos e confirmar que podem ser desativados sem afetar outros projetos. A nova instalação já deixou de utilizar fornecedores ou dependências do legado — prova [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346). Retirar o legado continua **bloqueado** por causa dos seus processos e da autorização de retirada.
