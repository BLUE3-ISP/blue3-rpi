# Blue3 RPI

Bootstrap interativo para Raspberry Pi OS Lite: prepara pacotes de desenvolvimento,
interfaces de sensores, espelho APT e sincronização de horário da Blue3. O único
script de provisionamento versionado neste repositório é [rpi_start.sh](rpi_start.sh).
Os antigos `blue3_rpi*` não estão neste checkout; o material histórico está
arquivado fora deste repositório.

## Estado e arquitetura

Revisão de fonte em 15/10/2026, base `e00540c` (`0.1.13`). O script executa todas
as etapas no sistema local, como root; não existe serviço Web, banco, firmware,
aplicação de leitura de sensores ou instalador de imagens neste projeto.

Ressalva sobre serviço Web: o script instala o metapacote `php`. No Debian com PHP 8.4,
`php8.4` depende de `libapache2-mod-php8.4 | php8.4-fpm | php8.4-cgi`; sem FPM ou CGI
já instalados, o APT escolhe a primeira alternativa e traz o Apache. O script não
configura nem desativa esse serviço. Conferido nas dependências do pacote, não em
execução num Raspberry Pi: confira no dispositivo com `systemctl status apache2`.

| Etapa | Comportamento implementado |
|---|---|
| Pré-requisitos | Bash com expansão de maiúsculas, root e `/etc/os-release` com ID `raspbian` ou `debian` |
| APT | Rewrites complete Debian archive URIs to `http://mirror.blue3.com.br/debian`, preserves security/other repository paths, then updates indexes and installs packages |
| Pacotes | Python/pip/venv, GPIO/SMBus/SPI, i2c-tools, curl, PHP CLI/curl, systemd-timesyncd, Git e editores |
| Horário | Sobrescreve timesyncd com `ntp.blue3.com.br` e fallback `pool.ntp.org`; tenta ativar o serviço/NTP |
| Sensores | Habilita I2C e SPI; pergunta por 1-Wire, com resposta padrão não |
| Interface | Pergunta por Desktop, padrão não; tenta metapacotes em ordem e depois ambiente mínimo |
| Log | Acrescenta em `/var/log/rpi_start.log`, com modo `640` |

O reconhecimento de hardware apenas avisa quando um arquivo de modelo existe e
não contém Raspberry Pi; não é uma validação rígida de placa, arquitetura ou versão.
A disponibilidade dos pacotes e do espelho precisa ser conferida no sistema-alvo.

## Preparar e executar

Use um Raspberry Pi destinado a esse provisionamento, com acesso administrativo,
rede e cópia recuperável das configurações existentes. Não é um comando de
consulta: modifica APT, horário, boot, módulos e alvo padrão do systemd.

```bash
# No dispositivo-alvo, a partir de um checkout revisado:
sudo bash rpi_start.sh
```

Não há flags, dry-run ou arquivo de ambiente do operador. Os endereços são
constantes do script; respostas são lidas do terminal. A revisão documental não
executou o bootstrap, instalou pacotes nem alterou um dispositivo.

## Configurações afetadas e recuperação

O script cria cópias `.blue3.bak` para os arquivos APT existentes e
`/etc/systemd/timesyncd.conf`. Uma nova execução pode sobrescrever a mesma cópia;
não há histórico de backups nem rollback automático. As alterações nos arquivos
`/boot/firmware/config.txt` ou `/boot/config.txt` e `/etc/modules` não ganham backup
por esse helper. Preserve esses arquivos antes de executar quando já houver configuração.

`raspi-config` é usado quando disponível; o fallback escreve as diretivas
`dtparam=i2c_arm=on`, `dtparam=spi=on` e, se escolhido, `dtoverlay=w1-gpio`.
O script não instala um programa de coleta nem testa sensores físicos.

## Verificar o resultado

Após revisar o log e reiniciar o dispositivo quando necessário, conferir:

```bash
systemctl get-default
timedatectl status
ls -l /dev/i2c-* /dev/spidev*
```

Em uma bancada apropriada, `i2cdetect -y 1` pode ajudar a conferir o barramento;
a resposta depende do hardware conectado. Verifique também o espelho APT e o
serviço de horário. O texto final “concluída” não prova que todas as chamadas
best-effort de systemd ou `modprobe` tiveram sucesso.

## Desenvolvimento e limites

Run `bash -n rpi_start.sh` for shell syntax and
`python3 -m unittest discover -s tests -v` for isolated APT source-file regression
tests. These checks do not execute the bootstrap or verify packages, networking,
boot, drivers, or sensors. The release workflow does not test hardware.

[Pontos de código e lacunas](docs/REVISAO-20261015.md) aguardam decisão separada.
Contribution instructions are in [AGENTS.md](AGENTS.md). From 0.1.14 on, repository
content and PRs are written in English (US); the Portuguese already here stays until it
is next touched. A documentation fix does not require a bump, per [version.md](version.md).
