# mathsh

A Linux shell where every command costs you a math problem.

Want to `ls`? Solve arithmetic. Want to `rm -rf`? Good luck with that integral.

```
  ███╗   ███╗ █████╗ ████████╗██╗  ██╗███████╗██╗  ██╗
  ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██╔════╝██║  ██║
  ██╔████╔██║███████║   ██║   ███████║███████╗███████║
  ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚════██║██╔══██║
  ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║███████║██║  ██║
  ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  pay your math debt to run commands.
```

## install

```bash
git clone https://github.com/potterpk/-mathsh.git
cd -mathsh
pip install -e .
mathsh
```

## how it works

Every command you type triggers a math challenge scaled to how dangerous the command is. Answer correctly and your command runs. Answer wrong and you get roasted.

## difficulty levels

| level     | example commands                   | problem types                         |
|-----------|------------------------------------|---------------------------------------|
| EASY      | `ls` `pwd` `echo` `cat` `whoami`   | addition, subtraction, multiplication |
| MEDIUM    | `cd` `mkdir` `git` `pip` `cp` `mv` | fractions, powers, percentages, modulo|
| HARD      | `sudo` `apt` `chmod` `ssh` `kill`  | quadratics, derivatives, prime factors|
| NIGHTMARE | `rm` `dd` `fdisk` `shred`          | integrals, systems of equations       |

## demo

```
mathsh ~ » ls

  [EASY] solve to proceed:
  47 + 38 = ?
  > 85
  ✓ correct. you may pass, nerd.

  README.md  src/  mathsh/

mathsh ~ » rm important_file.txt

  [NIGHTMARE] solve to proceed:
  ∫ 6x² + 2x dx = ?  (ignore +C)
  > 2x^3 + x^2
  ✓ wow, you actually know math.

mathsh ~ » rm important_file.txt

  [NIGHTMARE] solve to proceed:
  ∫ 4x³ dx = ?  (ignore +C)
  > x^3
  ✗ L + ratio + failed math
```

## answer format notes

- **fractions**: enter as decimal or fraction, e.g. `3/4` or `7/12`
- **powers**: `x^2` or `x**2` both work
- **quadratics**: comma-separated roots, e.g. `-2, 3`
- **prime factorization**: e.g. `2^2*3` for 12
- **systems of equations**: `x,y` format, e.g. `3,4`
- **integrals/derivatives**: omit `+C`, standard math notation

## built-in commands

| command       | action                              |
|---------------|-------------------------------------|
| `help`        | a suprise awaits                    |


## requirements

- Python 3.11+
- [sympy](https://www.sympy.org/) — for symbolic math checking
- [rich](https://github.com/Textualize/rich) — for colored terminal output
