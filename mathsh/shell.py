import os
from pathlib import Path

try:
    import readline  # noqa: F401 — enables arrow-key history on linux
except ImportError:
    pass

from mathsh.challenge import generate_challenge, get_difficulty
from mathsh.display import (
    console, get_prompt, print_banner, print_challenge,
    print_roast, print_success, print_help,
)
from mathsh.executor import execute_command


def main():
    print_banner()
    cwd = Path(os.getcwd())

    while True:
        try:
            user_input = console.input(get_prompt(str(cwd))).strip()
        except KeyboardInterrupt:
            console.print("\n  [dim](ctrl+c again or type exit to quit)[/]")
            continue
        except EOFError:
            console.print("[dim]\nbye[/]")
            break

        if not user_input:
            continue

        if user_input in ("exit", "quit", "q"):
            console.print("[dim]peace ✌️[/]")
            break

        if user_input == "help":
            print_help()
            continue

        difficulty = get_difficulty(user_input)
        question, check = generate_challenge(difficulty)

        print_challenge(difficulty, question)

        try:
            answer = input("  > ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n  [dim]aborted[/]")
            continue

        if check(answer):
            print_success()
            new_cwd = execute_command(user_input, cwd)
            if new_cwd:
                cwd = new_cwd
        else:
            print_roast()


if __name__ == "__main__":
    main()
