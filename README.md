[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Adnanhasim8/makefun-mang-pride-20261127/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Adnanhasim8/makefun-mang-pride-20261127/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

# One Line of Earned Pride

One quiet, earned moment of pride: a grandad plants a mango tree the year his grandchild is born, and decades of patient waiting finally land — this summer they pick its first fruit together, under its shade.

> Grandad planted the mango tree the year I was born; this summer we picked its first fruit together, under its shade.

The entry is a single line of 116 characters. It is a concrete scene with a real person, the pride earned inside the line by a long effort finally landing, and it lands in one read.

## How to run

Requires Python 3.13 (standard library only, no network at run time).

```sh
python3 main.py
```

This writes the entry to `entry.txt` in the output directory — `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`. Pass a different directory with `--out`, or print the entry after writing it with `--print`:

```sh
python3 main.py --out ./output --print
```

Before writing, the program asserts the entry is non-empty, exactly one line, and 1–200 characters long; after writing, it reads the file back and asserts the content equals the entry exactly.
