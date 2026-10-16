# Changelog

## 0.1.13 - Tira do README o link para repositório privado e avisa que o metapacote php pode puxar o Apache

O README apontava para o repositório privado de backup inicial: o link não abre para quem não é da casa e revelava o nome do repositório. Agora diz só que o material histórico está arquivado fora deste repositório. Acrescenta também a ressalva de que o `rpi_start.sh` instala o metapacote `php`, que no Debian com PHP 8.4 aceita o Apache (`libapache2-mod-php8.4`) como dependência, embora o projeto não tenha serviço Web. Correção documental sem bump, conforme version.md.

## 0.1.13 - Documenta o bootstrap atual do Raspberry Pi e seus limites

Revisa o fluxo completo, espelho/NTP, sensores, Desktop, backups e verificação. Consolida o português no README e registra achados de fonte sem alterar o script. Correção documental sem bump, conforme version.md.

O histórico anterior permanece em `version.md` e no Git.
