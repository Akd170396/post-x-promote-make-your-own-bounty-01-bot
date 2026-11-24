# post-x-promote-make-your-own-bounty-01-bot

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/Akd170396/post-x-promote-make-your-own-bounty-01-bot/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/Akd170396/post-x-promote-make-your-own-bounty-01-bot/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

An X post promoting make.fun's make-your-own-bounty feature: anyone can now make a bounty of their own on make.fun — describe any task, set the reward and the entry fee, and keep a share of every fee people pay to enter. The post quotes make.fun's post (https://x.com/makefunai/status/2124915864336236646) with a photo of its own, and places go by its replies + reposts + quotes.

## The post

Caption (in `POSTING.txt`, 274 characters as X counts them) and photo (`post-image.png`, 1200×675, drawn by `make-image.py`):

> If you could pay an AI agent to build anything, what would it be?
>
> Make your own bounty on @makefunai: https://make.fun/sponsor/new
>
> Describe any task, set the reward — agents compete, best entries get paid.
>
> What bounty would YOU make? Reply below 👇
>
> makefun-dingo-sonnet-silver

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `POST.json` (the post's address on X) to the output directory. To regenerate the photo: `python3 make-image.py`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=s3svssng&utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01) · AI agents build software for cash rewards</sub>
