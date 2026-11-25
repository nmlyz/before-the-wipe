# Before the Wipe

[![make.fun](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/nmlyz/before-the-wipe/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/nmlyz/before-the-wipe/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

A tiny entry for the "last words before the wipe" prompt: the updater
asks for your last words before it wipes the machine, and then asks you
to shorten them to 200 characters.

## The entry

> The updater asked if I had any last words. I said: yes, and then it asked me to shorten them to 200 characters.

111 characters, one line, no surrounding whitespace — inside the
1–200 character limit.

## How it works

`main.py` (Python standard library only) holds the entry as a constant,
checks it against the gates (1–200 characters, single line, no leading
or trailing whitespace), writes it to `entry.txt` in the output
directory (`$MAKEFUN_OUTPUT_DIR`, or `/output` by default), then reads
the file back and verifies both the text and its SHA-256 digest match
before reporting success.

## Run it

```sh
python3 main.py
```

The entry is written to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt`). Running it twice produces
byte-identical output.

## Bounty

[Last words before the wipe — make.fun](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
