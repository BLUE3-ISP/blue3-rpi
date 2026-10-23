# Changelog

## 0.1.15 - Preserve Debian security repositories when selecting the Blue3 mirror

Match the complete Debian archive URI instead of replacing its prefix inside
debian-security or other repository paths. Both legacy sources.list and deb822
sources keep their security channels while ordinary Debian archives move to
the Blue3 mirror. Isolated source-file tests cover both formats and repeated runs.

## 0.1.14 - the repository is written in English (US) from this version on, following its new owner on GitHub

On 23/10/2026 the repository moved from `BLUE3-ISP` to `samirhvbr`. The
language rule of [repodocs](https://github.com/samirhvbr/repodocs) is decided by
the owner on GitHub, and the Portuguese set is `BLUE3-ISP/*`,
`samirhvbr/blue3-intranet` and `samirhvbr/blue3-ai-login` — this repository is
no longer in it. Samir confirmed that reading the same day: it becomes English
(US). The local `origin` now points at `samirhvbr/blue3-rpi`.

The previous commit swapped the marked blocks. This one fixes the text outside
the markers that still prescribed Portuguese:

- `CLAUDE.md` and `AGENTS.md` — the commit line of the preamble, and a new
  `Language` section at the top that records the switch, the date and the
  decision (the twins stay identical below the H1);
- `version.md` §2 — the commit format and its rules;
- `README.md` — the contribution sentence.

Nothing else is translated. The Portuguese commit messages already in `git log`
and the Portuguese documents already in the tree stay as they are until they are
next touched; the edit then comes out in English.

## 0.1.14 - the echo blocks switch to English (US), following the owner on GitHub

The marked rules in `CLAUDE.md` and `AGENTS.md` are rewritten from the single
source at [samirhvbr/repodocs](https://github.com/samirhvbr/repodocs), and this
time the variant changes: the repository carried the Portuguese blocks, and
`origin` now names `samirhvbr/blue3-rpi`, which is outside the Portuguese set
(`BLUE3-ISP/*`, `samirhvbr/blue3-intranet`, `samirhvbr/blue3-ai-login`). The
language of a repository follows its owner on GitHub, so every block that has a
Portuguese variant arrives in English (US).

Only the blocks change in this commit. Text written outside the markers is the
repository's own, and history is not rewritten: Portuguese messages and
documents already there stay as they are until they are next touched.

## 0.1.13 - Tira do README o link para repositório privado e avisa que o metapacote php pode puxar o Apache

O README apontava para o repositório privado de backup inicial: o link não abre para quem não é da casa e revelava o nome do repositório. Agora diz só que o material histórico está arquivado fora deste repositório. Acrescenta também a ressalva de que o `rpi_start.sh` instala o metapacote `php`, que no Debian com PHP 8.4 aceita o Apache (`libapache2-mod-php8.4`) como dependência, embora o projeto não tenha serviço Web. Correção documental sem bump, conforme version.md.

## 0.1.13 - Documenta o bootstrap atual do Raspberry Pi e seus limites

Revisa o fluxo completo, espelho/NTP, sensores, Desktop, backups e verificação. Consolida o português no README e registra achados de fonte sem alterar o script. Correção documental sem bump, conforme version.md.

O histórico anterior permanece em `version.md` e no Git.
