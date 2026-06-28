import random
from rich.console import Console

console = Console()

DIFFICULTY_INFO = {
    1: ("EASY",      "green"),
    2: ("MEDIUM",    "yellow"),
    3: ("HARD",      "red"),
    4: ("NIGHTMARE", "bold red"),
}

ROASTS = [
    "nope lol",
    "bro said that with his whole chest 💀",
    "L + ratio + failed math",
    "back to 3rd grade fr",
    "command DENIED. skill issue.",
    "nah fam",
    "my grandma could do better and she's dead",
    "did you even try??",
    "wolfram alpha is free you know",
    "that's so wrong it's actually impressive",
    "calculator.net. use it.",
    "i'm not even mad, just disappointed",
    "what was that",
    "bro really fumbled the math",
    "you good??",
    "close only counts in horseshoes and hand grenades",
    "certified math fail moment",
    "the shell looked at that and said no",
    "rm -rf your math knowledge lmaooo",
]

SUCCESS_MSGS = [
    "fine. go.",
    "ok nerd. here.",
    "alright alright, go off",
    "wow you can do math. gold star or whatever",
    "grudgingly proceeding...",
    "i guess that's right. annoying.",
    "yeah ok. command unlocked.",
    "ugh fine",
]

BANNER = """\
  ███╗   ███╗ █████╗ ████████╗██╗  ██╗███████╗██╗  ██╗
  ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██╔════╝██║  ██║
  ██╔████╔██║███████║   ██║   ███████║███████╗███████║
  ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚════██║██╔══██║
  ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║███████║██║  ██║
  ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  pay your math debt to run commands. type [bold]help[/] to start.\
"""


def print_banner():
    console.print(BANNER, style="cyan")
    console.print()


def get_prompt(cwd: str) -> str:
    return f"[bold cyan]mathsh[/] [dim]{cwd}[/] [bold white]»[/] "


def print_challenge(difficulty: int, question: str):
    label, color = DIFFICULTY_INFO.get(difficulty, ("MEDIUM", "yellow"))
    # \[ and \] render as literal brackets inside Rich markup
    console.print(f"\n  [{color}]\\[{label}\\][/{color}] solve to proceed:")
    for line in question.split("\n"):
        console.print(f"  [bold white]{line}[/]")


def print_success():
    console.print(f"  [green]✓ {random.choice(SUCCESS_MSGS)}[/]\n")


def print_roast(correct_answer: str):
    console.print(f"  [red]✗ {random.choice(ROASTS)}[/]")
    console.print(f"  [dim]answer was: {correct_answer}[/]\n")


HELP_TROLL_INTROS = [
    "bro typed help 💀",
    "you really can't figure out a shell huh",
    "help??? really???",
    "we are SO cooked if you need help",
    "fine. here. don't make it weird.",
    "asking for help is actually sigma ngl",
    "ok ok ok fine i'll help",
    "you couldn't figure this out yourself? bold move",
]

HELP_TROLL_OUTROS = [
    "  godspeed. you'll need it.",
    "  now go touch grass",
    "  you're on your own now. i did my part.",
    "  if you still can't figure it out: cry about it",
    "  git gud or go home",
    "  any questions? google it.",
    "  good luck bestie 💅",
    "  don't make me explain it again",
]


def print_help():
    console.print(f"\n  {random.choice(HELP_TROLL_INTROS)}\n")
    console.print("""\
  [bold]how it works:[/]
  every linux command requires a math problem
  difficulty scales with how dangerous the command is:

    [green]EASY[/]      ls, pwd, echo, cat, whoami ...
    [yellow]MEDIUM[/]    cd, mkdir, cp, mv, git, pip ...
    [red]HARD[/]      sudo, apt, chmod, ssh, kill ...
    [bold red]NIGHTMARE[/] rm, dd, fdisk, shred ...

  get it wrong → command denied + roasted
  get it right → command runs normally

  [bold]built-in commands:[/]
  [cyan]help[/]       this message (you're reading it, genius)
""")
    console.print(f"{random.choice(HELP_TROLL_OUTROS)}\n")
