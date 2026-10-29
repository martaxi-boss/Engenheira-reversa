# Auditoria comparativa do motor FINAL com o original do autor — 29/10/2026

## Âmbito, identidade e provas

**Comparador:** código original do autor [`morluto/rea` no commit imutável `160d821ac9a0310afcb8d1fc427862dd6508add5`](https://github.com/morluto/rea/tree/160d821ac9a0310afcb8d1fc427862dd6508add5), não a instalação antiga `/opt/rea-reversa/rea`. A versão do original neste commit é `rea-agents 6.8.0`; trata-se da referência do autor e não de uma comparação com o legado.

**Motor final real na VPS:** `/home/ubuntu/rea-original-upstream-680`. Runtime independente: `/home/ubuntu/rea-final-runtime`.

**Provas ao vivo, somente leitura:** [auditoria de dependências, programas e Doctor 40971914250](https://github.com/martaxi-boss/VPS/actions/runs/40971914250) e [causas de Doctor por fornecedor 40972191490](https://github.com/martaxi-boss/VPS/actions/runs/40972191490).

Foram verificados o SHA Git do motor final, hashes de módulos compilados, identidade `package.json`, correspondência exata com o `package.json` do commit do autor, concordância do `package-lock.json` e os três ficheiros fundamentais inalterados. A ferramenta oficial `scripts/check-dependency-install.mjs` terminou com `exit=0`.

**Conclusão inequívoca:** `0` dependências Node.js obrigatórias do autor em falta. Não se justifica reinstalar o motor, Node, Java, Ghidra, JADX, Unblob ou qualquer pacote npm obrigatório.

## Ambiente Linux observado

| Elemento | Resultado |
| --- | --- |
| Distribuição | Ubuntu 24.04.4 LTS |
| Arquitetura | Linux x86_64 |
| Kernel | 6.8.0-147-generic |
| Memória total | 7.57 GiB |
| Espaço livre após organização | 23.71 GiB |
| Node.js | v24.22.1 — compatível com o requisito `^22.23.4 || ^24.22.1 || >=26.12.1` |
| Java/JDK | openjdk version "21.0.12.1" 2026-08-18 LTS |
| Python | Python 3.12.3 |
| npm | 10.9.8 |
| `procps ps` obrigatório | ps from procps-ng 4.0.4; `ps -o pid= -p PID` PASS |
| Ferramentas de compilação | GCC e G++ presentes; Clang e CMake não detetados no `PATH` |
| Ecrã e sessão gráfica | Sem `DISPLAY`/Wayland; Xvfb instalado |
| Conexão Android físico | **Não testada**, não inferir ADB ligado |
| Código original alterado | Não — pacote original e ficheiros-chave coincidem |

## Matriz exaustiva das dependências Node.js do original

- Obrigatórias em `package.json`: **42/42 presentes**, nenhuma ausente e nenhuma versão divergente.
- Opcionais em `package.json`: **Frida 17.23.2** presente com versão `17.23.2`.
- Desenvolvimento: **27/27 presentes**. Os aliases `typescript-termux` e `typescript6` usam especificadores `npm:typescript@...`; os números de versão instalados são os esperados, não são lacunas nem dependências a reinstalar.
- Verificador oficial de dependências: `exit 0`.

### Todas as 42 dependências obrigatórias

| Pacote npm do autor | Versão declarada | Estado na VPS |
| --- | --- | --- |
| `@babel/parser` | `8.0.4` | Instalado e versão coincidente |
| `@babel/types` | `8.0.4` | Instalado e versão coincidente |
| `@bufbuild/protobuf` | `2.16.0` | Instalado e versão coincidente |
| `@clack/prompts` | `1.7.0` | Instalado e versão coincidente |
| `@electron/asar` | `4.2.0` | Instalado e versão coincidente |
| `@jridgewell/trace-mapping` | `0.3.31` | Instalado e versão coincidente |
| `@lydell/node-pty` | `1.1.0` | Instalado e versão coincidente |
| `@modelcontextprotocol/client` | `2.3.1` | Instalado e versão coincidente |
| `@modelcontextprotocol/server` | `2.3.1` | Instalado e versão coincidente |
| `@msgpack/msgpack` | `3.1.3` | Instalado e versão coincidente |
| `@xmldom/xmldom` | `0.9.12` | Instalado e versão coincidente |
| `@xterm/addon-serialize` | `0.14.0` | Instalado e versão coincidente |
| `@xterm/headless` | `6.0.0` | Instalado e versão coincidente |
| `@zip.js/zip.js` | `2.15.0` | Instalado e versão coincidente |
| `ajv` | `8.20.0` | Instalado e versão coincidente |
| `ajv-formats` | `3.0.1` | Instalado e versão coincidente |
| `canonicalize` | `3.0.0` | Instalado e versão coincidente |
| `cborg` | `6.1.3` | Instalado e versão coincidente |
| `cross-spawn` | `7.0.6` | Instalado e versão coincidente |
| `diff` | `9.0.0` | Instalado e versão coincidente |
| `evmole` | `0.9.3` | Instalado e versão coincidente |
| `har-schema` | `2.0.0` | Instalado e versão coincidente |
| `ignore` | `7.0.6` | Instalado e versão coincidente |
| `incur` | `0.6.1` | Instalado e versão coincidente |
| `isomorphic-git` | `1.38.7` | Instalado e versão coincidente |
| `jsonc-parser` | `3.3.1` | Instalado e versão coincidente |
| `lossless-json` | `4.3.1` | Instalado e versão coincidente |
| `openpgp` | `6.3.2` | Instalado e versão coincidente |
| `parse5` | `8.0.1` | Instalado e versão coincidente |
| `pino` | `10.4.0` | Instalado e versão coincidente |
| `playwright-core` | `1.58.2` | Instalado e versão coincidente |
| `plist` | `5.0.0` | Instalado e versão coincidente |
| `saxes` | `6.0.0` | Instalado e versão coincidente |
| `semver` | `7.8.5` | Instalado e versão coincidente |
| `smol-toml` | `1.9.0` | Instalado e versão coincidente |
| `stream-chain` | `4.2.6` | Instalado e versão coincidente |
| `stream-json` | `3.7.0` | Instalado e versão coincidente |
| `tokenx` | `1.3.0` | Instalado e versão coincidente |
| `write-file-atomic` | `7.0.0` | Instalado e versão coincidente |
| `ws` | `8.21.0` | Instalado e versão coincidente |
| `yaml` | `2.9.0` | Instalado e versão coincidente |
| `zod` | `4.4.3` | Instalado e versão coincidente |

### Dependência opcional

| Pacote | Versão declarada | Estado |
| --- | --- | --- |
| `frida` | `17.23.2` | Instalado `17.23.2`; sem prova de dispositivo/alvo ligado |

### Todas as 27 dependências de desenvolvimento (não obrigatórias em produção)

| Pacote do autor | Versão declarada |
| --- | --- |
| `@fast-check/vitest` | `0.5.0` |
| `@stryker-mutator/core` | `10.0.0` |
| `@stryker-mutator/typescript-checker` | `10.0.0` |
| `@stryker-mutator/vitest-runner` | `10.0.0` |
| `@types/cross-spawn` | `6.0.6` |
| `@types/node` | `26.6.4` |
| `@types/semver` | `7.7.1` |
| `@types/write-file-atomic` | `4.0.3` |
| `@types/ws` | `8.18.1` |
| `@vitest/coverage-v8` | `5.0.3` |
| `husky` | `9.1.7` |
| `jscpd` | `5.0.12` |
| `knip` | `6.39.0` |
| `lint-staged` | `16.4.0` |
| `oxfmt` | `0.72.0` |
| `oxlint` | `1.87.0` |
| `oxlint-tsgolint` | `7.0.2005` |
| `release-please` | `17.3.0` |
| `rolldown` | `1.2.12` |
| `tsrs` | `0.18.0-ts7.1.0-dev.20260929` |
| `tsx` | `4.23.15` |
| `turbo` | `2.11.7` |
| `typescript` | `7.0.2` |
| `typescript-termux` | `npm:typescript@5.9.3` |
| `typescript6` | `npm:typescript@6.0.3` |
| `vitepress` | `1.6.4` |
| `vitest` | `5.0.3` |

Estes pacotes foram detetados como presentes. Não confundir dependências de desenvolvimento com requisitos para executar o motor já compilado.

## Inventário real de 26 componentes externos e programas

**26/26 existentes** nos caminhos indicados pela ponte operacional. `present` e `--version` **não certificam todas as funcionalidades**.

| Componente | Versão / identificação verificada | Nível de prova |
| --- | --- | --- |
| 7-Zip | 7-Zip 23.01 (x64) : Copyright (c) 1999-2023 Igor Pavlov : 2023-06-20 | Presente; opção de versão usada retornou 7; não é falha de instalação |
| ADB | Android Debug Bridge version 1.0.41 | Presença/versionamento; função não certificada neste ensaio |
| APKTool | 2.7.0-dirty | Decodificação de APK anterior PASS |
| Binwalk | binwalk 3.1.0 | Inspeção firmware real anterior PASS |
| Chromium | Google Chrome for Testing 145.0.7632.6 | Instalado na árvore antiga; sandbox/sessão não certificado |
| Cutter | 2.5.0 (nome do pacote) | GUI presente; integração sessão não certificada |
| .NET | 10.0.114 | Presença/versionamento; função não certificada neste ensaio |
| FFmpeg | ffmpeg version 6.1.1-3ubuntu5 Copyright (c) 2000-2023 the FFmpeg developers | Presença/versionamento; função não certificada neste ensaio |
| Frida Node binding | 17.23.2 (npm) | Binding npm presente; análise com dispositivo não testada |
| GDB | GNU gdb (Ubuntu 15.1-1ubuntu1~24.04.1) 15.1 | Presença/versionamento; função não certificada neste ensaio |
| Ghidra | 12.1.4 (Doctor) | Doctor PASS; análise ELF real PASS |
| Hopper | Binário presente; versão recusada pelo Doctor | Doctor FAIL por versão; fornecedor opcional |
| ILSpy | ilspycmd: 11.2.0.10050 | Presença/versionamento; função não certificada neste ensaio |
| JADX Headless | JAR 0.7.1 (Doctor) | Doctor PASS; APK/classe/método reais PASS |
| Java 21 | openjdk version 21.0.12.1 2026-08-18 LTS | Doctor Ghidra PASS |
| Kuna | kuna 1.833 | Doctor PASS; versão verificada |
| Mitmproxy/mitmdump | Mitmproxy: 12.2.3 | Presença/versionamento; função não certificada neste ensaio |
| Node.js | v24.22.1 | Versionado e em uso |
| Pwndbg gdbinit | script presente, sem execução direta | Presença/versionamento; função não certificada neste ensaio |
| Pwntools | Python 3.12 (ambiente), módulo presente | Presença/versionamento; função não certificada neste ensaio |
| Rizin | rizin 0.9.1 @ linux-x86-64 | Presença/versionamento; função não certificada neste ensaio |
| sigrok-cli | sigrok-cli 0.7.2 | Presença/versionamento; função não certificada neste ensaio |
| TShark | TShark (Wireshark) 4.2.2 (Git v4.2.2 packaged as 4.2.2-1.1build3). | Presença/versionamento; função não certificada neste ensaio |
| Unblob | 26.6.4 | Extração real e Python próprio PASS |
| Wakaru | wakaru 1.14.0 | Presença/versionamento; função não certificada neste ensaio |
| WABT wasm2wat | 1.0.42 | Presença/versionamento; função não certificada neste ensaio |

Apenas **Chromium** continua com caminho explicitamente dentro de `/opt/rea-reversa/providers` no inventário operacional. Não foi copiado porque a sessão/sandbox de Chromium tinha limitações de política. Não contornar AppArmor.

## Diagnóstico `doctor --provider` do original

O Doctor original foi executado em escopos explícitos e com os caminhos próprios do motor FINAL:

| Fornecedor | Estado | Causa / observação |
| --- | --- | --- |
| ghidra | PASS | Nenhuma falha no âmbito selecionado |
| jadx | PASS | Nenhuma falha no âmbito selecionado |
| kuna | PASS | Nenhuma falha no âmbito selecionado |
| hopper | Não pronto | hopper-version: /opt/hopper/bin/Hopper |
| ida | Não pronto | ida-registration: IDA MCP registration is not configured. |

**Interpretação:** Ghidra, JADX e Kuna estão prontos no escopo selecionado. Hopper está fisicamente instalado, mas a verificação `hopper-version` falha. IDA não tem registo MCP configurado. São **alternativas opcionais**; o motor não precisa dos dois para usar Ghidra/Kuna.

O Doctor global pode marcar `environment_healthy=false` também por `skill:identity` não encontrado **no sistema Linux**. Isso não significa que a Skill ChatGPT esteja desligada: as chamadas reais à Skill passaram em [40970285268](https://github.com/martaxi-boss/VPS/actions/runs/40970285268) (health 4/4) e [40970395308](https://github.com/martaxi-boss/VPS/actions/runs/40970395308) (APK 3/3). Não instalar outra Skill/Plugin/MCP na VPS para satisfazer um indicador de configuração do agente.

## Lacunas: o que falta instalar neste Ubuntu

### Essencial para o motor FINAL que já funciona: **nada obrigatório**

| Categoria | Ausentes obrigatórios | Resultado |
| --- | ---: | --- |
| 42 pacotes npm `dependencies` | 0 | PASS |
| Frida opcional do `package.json` | 0 | Presente (não equivale a teste em dispositivo) |
| Versão Node, Java, `ps` e código original | 0 | Compatíveis / PASS |
| Análise Ghidra, JADX e Unblob com ficheiros de teste | 0 | Funções reais comprovadas |

### Extras gratuitos Linux que não apareceram no `PATH`

- **`clang`** — não localizado no `PATH`. É compatível com Ubuntu, mas **não é requisito do núcleo**. Instalar apenas quando houver trabalho que exija essa ferramenta específica.
- **`cmake`** — não localizado no `PATH`. É compatível com Ubuntu, mas **não é requisito do núcleo**. Instalar apenas quando houver trabalho que exija essa ferramenta específica.
- **`lldb`** — não localizado no `PATH`. É compatível com Ubuntu, mas **não é requisito do núcleo**. Instalar apenas quando houver trabalho que exija essa ferramenta específica.
- **`ltrace`** — não localizado no `PATH`. É compatível com Ubuntu, mas **não é requisito do núcleo**. Instalar apenas quando houver trabalho que exija essa ferramenta específica.

Ausência do `PATH` não prova que o software não exista noutro diretório. `gcc`, `g++`, `strace`, `radare2`, `objdump`, `readelf`, `file` e `Xvfb` **já foram encontrados**.

### Opcionais, pagos ou com condições ainda não satisfeitas

- **Hopper:** binário presente, mas `doctor --provider hopper` **FAIL (`hopper-version`)**. Produto comercial/demonstração com limitações; não há necessidade de o instalar para as análises já feitas pelo Ghidra.
- **IDA:** programa não encontrado no `PATH` e **registo IDA MCP ausente**. Não é um requisito do REA; não criar MCP nem comprar licença para aumentar contagens.
- **JEB:** não encontrado no `PATH`; produto comercial opcional, não obrigatório.
- **Chromium:** executável presente e versão lida, mas não há prova de sessão CDP/sandbox funcional sob AppArmor; caminho ainda partilhado.
- **Cutter:** AppImage presente, mas sem certificação abrangente de sessão GUI ligada ao REA.
- **Frida:** binding instalado, mas testes reais com dispositivo/alvo não executados.
- **Hopper, Chromium e GUI:** não são lacunas de npm nem justificam alterar as proteções do sistema.

### Não aplicáveis a esta VPS

Componentes exclusivos de Windows, macOS/Xcode e integração com iOS físico não devem ser instalados no Ubuntu para elevar artificialmente uma contagem. O ADB instalado não significa que exista um dispositivo Android ligado.

## Qualidade e limites

- O checkout final corresponde ao commit imutável do autor e o `package.json` é igual ao original.
- [40968620168](https://github.com/martaxi-boss/VPS/actions/runs/40968620168): 8/8 testes de execução com `node_modules` próprio.
- [40969647492](https://github.com/martaxi-boss/VPS/actions/runs/40969647492): 11/11 verificações reais de Ghidra, JADX, Unblob e limpeza de processos.
- [40970111752](https://github.com/martaxi-boss/VPS/actions/runs/40970111752): Unblob via Python do runtime independente.
- [40970285268](https://github.com/martaxi-boss/VPS/actions/runs/40970285268): 4/4 comandos health da Skill.
- [40970395308](https://github.com/martaxi-boss/VPS/actions/runs/40970395308): 3/3 análises APK reais via Skill.
- [40971914250](https://github.com/martaxi-boss/VPS/actions/runs/40971914250): auditoria atual de 42 dependências + 26 componentes.
- [40972191490](https://github.com/martaxi-boss/VPS/actions/runs/40972191490): causas explícitas das falhas opcionais no Doctor.

**Nenhuma auditoria de presença certifica automaticamente todas as 229 ferramentas MCP do catálogo.** Os fornecedores não ensaiados no alvo apropriado continuam com estatuto `INSTALADO, FUNCIONALIDADE NÃO TESTADA`.

## Retirada futura da instalação antiga: questão distinta de instalar dependências

A auditoria de processos [40971066042](https://github.com/martaxi-boss/VPS/actions/runs/40971066042) encontrou **um processo Node ativo que referencia diretamente o motor antigo** e outro processo Python com referência a caminhos antigos. A remoção continua bloqueada até identificar os proprietários/serviços, confirmar que nenhum consumidor precisa da instalação antiga e validar um plano reversível. Nenhuma pasta nem serviço legado foi eliminado nesta auditoria.

## Ordem de ação baseada em necessidade

1. **Não reinstalar dependências obrigatórias nem fornecedores já funcionais.**
2. Se a finalidade for diagnóstico nativo mais avançado, considerar `lldb`, `ltrace`, `clang` ou `cmake` apenas quando um cenário real exigir.
3. Tratar Hopper/IDA/JEB como **opcionais**, sem custos ou novos MCPs por rotina. Não alterar AppArmor para forçar Chromium.
4. Para libertar espaço: auditar os dois consumidores ativos e dependências opcionais antes de qualquer eliminação. Ler [RETIRADA_LEGADO.md](RETIRADA_LEGADO.md).

Nenhuma instalação, eliminação, nova Skill, motor, workflow ou MCP foi realizada **nesta auditoria**. O estudo baseia-se na versão original exata, na árvore atual da VPS e nos logs novos das duas execuções.

## Atualização posterior — separação completa da execução face ao legado (29/10/2026)

Esta auditoria de dependências foi feita antes de terminar a migração de componentes opcionais. A informação histórica acima mantém-se válida para a hora da captura, **mas deixou de representar a configuração atual**.

- Copiados Chromium, ILSpy, Pwndbg e Pwntools para o runtime privado final em [40974091601](https://github.com/martaxi-boss/VPS/actions/runs/40974091601), com correção de ligações internas do Pwndbg.
- Normalizadas referências antigas em lançadores/venvs das cópias em [40974350944](https://github.com/martaxi-boss/VPS/actions/runs/40974350944).
- O motor final passou health 4/4, com **0 fornecedores ativos apontados à instalação antiga**, em [40974532931](https://github.com/martaxi-boss/VPS/actions/runs/40974532931).
- Auditoria final [40974645346](https://github.com/martaxi-boss/VPS/actions/runs/40974645346): 290 symlinks examinados e nenhum apontado ao legado; 0 referências de launcher/config nos ficheiros analisados; 0 caminhos do inventário final para o antigo.
- Análise APK 3/3 PASS em [40974717355](https://github.com/martaxi-boss/VPS/actions/runs/40974717355); bloqueio de regressão no bridge comprovado em [40974869693](https://github.com/martaxi-boss/VPS/actions/runs/40974869693).
- Hopper foi **excluído da lista de fornecedores ativos do motor final**, por falta de prontidão/licença. A contagem operacional passou a 25 componentes (inclui o binding Frida); o inventário histórico de 26 incluía Hopper por presença no host.

A dependência de ferramentas comuns do Ubuntu em `/usr/bin` não é uma dependência do motor antigo, mas sim a base partilhada do sistema operativo. A eliminação do legado continua bloqueada enquanto os processos próprios antigos estiverem em execução.
