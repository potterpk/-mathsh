import os
import subprocess
from pathlib import Path


def execute_command(command: str, cwd: Path) -> Path | None:
    """Run a shell command. Returns new cwd if cd changed it, else None."""
    parts = command.strip().split()
    if not parts:
        return None

    if parts[0] == "cd":
        return _handle_cd(parts, cwd)

    try:
        subprocess.run(
            command,
            shell=True,
            cwd=str(cwd),
            env={**os.environ, "PWD": str(cwd)},
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        print("mathsh: command timed out (60s)")
    except Exception as e:
        print(f"mathsh: {e}")

    return None


def _handle_cd(parts: list[str], cwd: Path) -> Path | None:
    target = parts[1] if len(parts) > 1 else str(Path.home())

    if target == "-":
        prev = os.environ.get("OLDPWD")
        if prev:
            return Path(prev).resolve()
        print("mathsh: cd: OLDPWD not set")
        return None

    try:
        new_cwd = (cwd / target).resolve()
        if new_cwd.is_dir():
            os.environ["OLDPWD"] = str(cwd)
            return new_cwd
        print(f"mathsh: cd: {target}: No such file or directory")
    except Exception as e:
        print(f"mathsh: cd: {e}")

    return None
