# Dois motores independentes — certificação da separação (29/10/2026)

## Regra do proprietário

**O motor FINAL não usa dependências nem fornecedores instalados exclusivamente para o 6.8 anterior.** Cada projeto tem o seu código e runtime separados. Não reintroduzir ligações ao legado. O motor anterior foi desativado e eliminado em 30/10/2026, após verificação do checkout final.

## Estrutura na VPS

| Componente | Caminho do FINAL |
| --- | --- |
| Código original imutável do autor | `/home/ubuntu/rea-original-upstream-680` |
| Dependências Node do motor | `/home/ubuntu/rea-final-runtime/node_modules` |
| Ghidra, JDK, Node, JADX, Rizin, Binwalk, Unblob, Chromium etc. | `/home/ubuntu/rea-final-runtime/vendors` |
| ILSpy, Pwndbg e Pwntools em instalações próprias | `/home/ubuntu/rea-final-runtime/optional` |
| Lançador independente Unblob | `/home/ubuntu/rea-final-runtime/bin/unblob` |

A arquitetura foi verificada contra o autor `morluto/rea`, commit `160d821ac9a0310afcb8d1fc427862dd6508add5`, **não** comparada ou instalada por cima da árvore antiga.

## Evidências reais na VPS

| Prova | ID GitHub Actions | Resultado |
| --- | --- | --- |
| Cópias privadas de Chromium, ILSpy, Pwndbg, Pwntools | [40974091601](https://github.com/martaxi-boss/VPS/actions/runs/40974091601) | PASS |
| Reescrita de shebangs, venv e metadata das **cópias privadas** | [40974350944](https://github.com/martaxi-boss/VPS/actions/runs/40974350944) | PASS |
| Health Skill → GitHub Actions → SSH → CLI | [40974532931](https://github.com/martaxi-boss/VPS/actions/runs/40974532931) | 4/4 PASS |
| Auditoria de 9 252 itens do checkout + 64 713 do runtime | [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346) | 0 links ao legado, 0 caminhos ativos antigos |
| APK com análise de pacote/classe/método | [40974717355](https://github.com/martaxi-boss/VPS/actions/runs/40974717355) | 3/3 PASS, 0 cleanup_incomplete |
| Invariante de bloqueio de fornecedor legado no bridge | [40974869693](https://github.com/martaxi-boss/VPS/actions/runs/40974869693) | 4/4 PASS |

### Resultados da auditoria de ligações

- **0/290 symlinks** da árvore final apontam para `/opt/rea-reversa`.
- **0 referências antigas** detetadas entre lançadores/configurações de pequena dimensão incluídos no scanner.
- **0 entradas de fornecedor ativo** do motor final com caminho para `/opt/rea-reversa`.
- O motor usa `node_modules` da própria estrutura, sem apontar para `/opt/rea-reversa/rea/node_modules`.
- O bridge operacional recusa ordens quando deteta um fornecedor apontado à instalação antiga ou uma dependência opcional reutilizada da árvore `~/.local/share/rea-optional-*`.

O teste é limitado aos diretórios e ficheiros examinados. Não demonstra funcionamento de todas as ferramentas MCP nem certifica a sessão gráfica de Chromium.

### O que **não** é partilha com o motor antigo

Comandos do Ubuntu como `/usr/bin/gdb`, `/usr/bin/ffmpeg`, `/usr/bin/adb` ou o Python de base pertencem ao próprio sistema operativo e podem servir várias aplicações. **Isto não cria uma dependência entre o motor final e o 6.8.** Um isolamento completo das bibliotecas e pacotes do próprio Ubuntu exigiria um ambiente de sistema separado (como um contentor com imagem própria); isso não foi criado nem é necessário para separar os motores.

### Atualização de retirada — 30/10/2026

A auditoria anterior [40971066042](https://github.com/martaxi-boss/VPS/actions/runs/40971066042) identificou dois processos do legado. O proprietário identificou-os como `rea-reversa-mcp.service` e `rea-mcp-oauth.service`, parou-os e desativou-os. O teste posterior mostrou ausência de processos antigos, `/opt/rea-reversa` completamente eliminado e a CLI `providers --json` do motor final a funcionar, com 29 GB livres. Prova: capturas do terminal fornecidas ao projeto em 30/10/2026.

O repositório GitHub atual já não inclui `rea/`, `certifications/` ou os cinco submódulos históricos antigos; manteve `engenharia-reversa/original` fixado no commit do autor. A ponte `martaxi-boss/VPS` e o histórico Git não foram apagados. Não foram instalados motores, servidores, MCPs, DNS ou workflows adicionais nesta retirada.
