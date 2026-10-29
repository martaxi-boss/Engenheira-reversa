# Dois motores independentes — certificação da separação (29/10/2026)

## Regra do proprietário

**O motor FINAL não usa dependências nem fornecedores instalados exclusivamente para o 6.8 anterior.** Cada projeto tem o seu código e runtime separados. Não reintroduzir ligações ao legado. O motor anterior não foi atualizado nem desinstalado.

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

### O que ainda impede apagar o projeto antigo

A [auditoria 40971066042](https://github.com/martaxi-boss/VPS/actions/runs/40971066042) identificou dois processos com referências ao legado, um deles associado diretamente ao motor antigo. São **processos do sistema antigo**, não dependências do final; não foram interrompidos.

A remoção das suas pastas, dos fornecedores antigos, dos submódulos `rea/` e do histórico Git exige avaliação de consumidores ativos e uma operação de retirada separada. A independência do final já não depende da eliminação do antigo.

Não foram instalados novos motores, servidores, MCPs, coordenadores, DNS ou workflows. O GitHub mantém as árvores de código antigo e final em pastas distintas até a futura retirada aprovada.
