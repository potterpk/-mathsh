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
    "that's not even close lmao",
    "my grandma could do better and she's dead",
    "bro really said that with confidence 💀",
    "L + ratio + failed math",
    "back to 3rd grade with you",
    "command DENIED. skill issue.",
    "nah fam that's wrong",
    "are you sure you graduated?",
    "the audacity to get that wrong",
    "even my cat knows that's wrong",
    "did you even try?",
    "wolfram alpha is free you know",
    "calculator.net exists for a reason",
]

SUCCESS_MSGS = [
    "correct. you may pass, nerd.",
    "not bad. running your command...",
    "ok fine. here you go.",
    "surprisingly correct. proceeding...",
    "wow, you actually know math.",
    "begrudgingly running your command...",
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


def print_roast():
    console.print(f"  [red]✗ {random.choice(ROASTS)}[/]\n")


HELP_TROLL_INTROS = [
    "oh you need [bold]help[/]? shocking. truly.",
    "bro typed help 💀 we are so cooked",
    "you really couldn't figure it out yourself huh",
    "the fact that you need help with a SHELL is sending me",
    "help??? in THIS economy???",
    "reading the manual? in 2025? based actually",
    "don't worry babe here's your little tutorial 🫶",
    "sigma male moment: asking for help. respect.",
]

HELP_TROLL_OUTROS = [
    "  goodluck bestie you're gonna need it 💅",
    "  now go touch grass after you solve that integral",
    "  no more hand holding. you're on your own. godspeed.",
    "  this has been your ted talk. you're welcome.",
    "  if you still can't figure it out: cry about it",
    "  skill issue detected. please git gud.",
    "  any questions? too bad. figure it out.",
    "  erm actually 🤓 you should know this already",
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
