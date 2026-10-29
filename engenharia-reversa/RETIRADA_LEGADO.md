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
- [ ] **Fornecedor opcional Chromium:** ainda aponta para `/opt/rea-reversa/providers/chromium-playwright-1.58.2` e o sandbox está bloqueado; não contornar AppArmor nem declarar este fornecedor certificado.
- [ ] **Hopper:** pacote externo existente, versão/build não certificado para o motor, sem licença paga. Não adicionar aos fornecedores certificados por simples presença.
- [ ] **Referências internas:** fazer leitura final de scripts, configurações, virtualenvs e symlinks para verificar que nenhuma operação necessária continua a depender da instalação antiga. Não confundir 26 componentes presentes com certificação integral das 229 ferramentas.
- [ ] **Verificação de serviço pós-retirada:** plano de rollback, prova de saúde e ensaios com entradas controladas após migração dos consumidores.
- [ ] **Autorização separada de remoção:** somente depois de todas as portas acima estarem resolvidas, identificar caminhos exatos autorizados, estimativa de espaço libertado e plano de reversão.

## GitHub

O projeto final está em `engenharia-reversa/` com o original fixado como submódulo. O antigo está em `rea/` (árvore Git e respetivos submódulos), `certifications/` e histórico. **Não apagar ainda**. Quando for expressamente aprovado, preparar um PR que remova apenas os caminhos legados e as secções legadas de `.gitmodules`, preservando o submódulo final, código e evidências essenciais. Remover ficheiros do HEAD diminui o checkout, mas não elimina automaticamente o histórico Git nem garante uma redução igual do armazenamento remoto; não executar reescrita de histórico/force push por rotina.

## Regras

Não criar outro motor, não usar Codex, não instalar MCP adicional, não mexer noutros projetos. A ligação operacional é o workflow SSH já existente em `martaxi-boss/VPS`; GitHub é fonte documental, não um substituto do teste real.
