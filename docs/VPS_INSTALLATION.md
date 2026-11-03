# Engenheira-reversa — instalacao isolada VPS

**Repositorio GitHub:** `martaxi-boss/Engenheira-reversa`.
**Instalacao fisica na VPS:** `/srv/projects/Engenheira-reversa` (grafia exatamente igual ao repo).

Esta pasta e a antiga instalacao **REA Trial** (2 529 660 928 bytes). O clone Git esta em `repository/`; as ferramentas, artefactos, arquivos e outros componentes continuam dentro da mesma pasta, sem copiar para outros projetos.

A localizacao antiga `/home/ubuntu/.local/share/rea-chatgpt-trial` e agora apenas uma **ligacao temporaria de compatibilidade**. O repositorio Git, a revisao instalada e as suas alteracoes locais ficaram intactos; os processos e servicos principais da VPS nao mudaram de estado.

Prova da migracao: [GitHub Actions #41715190029](https://github.com/martaxi-boss/VPS/actions/runs/41715190029). O processo REA terminou com codigo zero, mas o resultado da observacao incluiu `settlement: unverifiable`; confirmar a integridade apos novo arranque antes de remover a ligacao antiga.

**Este Trial nao e o REA FINAL.** O motor FINAL em `/home/ubuntu/rea-final-runtime`, o clone upstream `/home/ubuntu/rea-original-upstream-680` e as respetivas evidencias sao instalacoes distintas e nao foram movidas, integradas ou eliminadas neste passo.

Nao publicar sessoes, credenciais, backups de execucao ou artefactos gerados no GitHub. Ainda falta certificar um ciclo completo de instalacao/reinstalacao/desinstalacao independente e remover referencias ao caminho legado.
