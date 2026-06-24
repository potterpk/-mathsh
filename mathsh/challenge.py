import random
import sympy as sp
from sympy import symbols, Rational
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

x = symbols("x")

# parse_expr with a restricted local_dict avoids the bare eval() inside sp.sympify
_PARSE_TRANSFORMS = standard_transformations + (implicit_multiplication_application,)


def _safe_parse(raw: str):
    cleaned = raw.strip().replace("^", "**")
    return parse_expr(cleaned, local_dict={"x": x}, transformations=_PARSE_TRANSFORMS)


def get_difficulty(command: str) -> int:
    parts = command.strip().split()
    if not parts:
        return 1
    cmd = parts[0].lower()
    if cmd == "sudo" and len(parts) > 1:
        cmd = parts[1].lower()

    easy = {"ls", "pwd", "echo", "cat", "man", "which", "whoami", "date", "clear",
            "history", "help", "type", "alias", "printenv", "uname"}
    medium = {"cd", "mkdir", "rmdir", "touch", "cp", "mv", "grep", "find", "git",
              "pip", "pip3", "python", "python3", "nano", "vim", "nvim", "less",
              "more", "head", "tail", "wc", "sort", "uniq", "diff", "tar", "zip",
              "unzip", "chmod", "chown", "ln"}
    hard = {"sudo", "apt", "apt-get", "dnf", "pacman", "yum", "brew", "npm", "yarn",
            "systemctl", "service", "curl", "wget", "ssh", "scp", "rsync", "kill",
            "killall", "pkill", "iptables", "ufw", "mount", "umount"}
    nightmare = {"rm", "dd", "mkfs", "fdisk", "shred", "wipefs", "parted", "hdparm"}

    if cmd in easy:
        return 1
    elif cmd in medium:
        return 2
    elif cmd in hard:
        return 3
    elif cmd in nightmare:
        return 4
    return 2


def generate_challenge(difficulty: int):
    pool = {
        1: [_add, _subtract, _multiply],
        2: [_fraction, _power, _percentage, _modulo],
        3: [_quadratic, _derivative, _prime_factor],
        4: [_integral, _system_of_equations, _hard_derivative],
    }
    return random.choice(pool.get(difficulty, pool[2]))()


# --- Level 1: arithmetic ---

def _add():
    a, b = random.randint(10, 99), random.randint(10, 99)
    return f"{a} + {b} = ?", _num_check(a + b)

def _subtract():
    a = random.randint(20, 99)
    b = random.randint(1, a)
    return f"{a} - {b} = ?", _num_check(a - b)

def _multiply():
    a, b = random.randint(2, 15), random.randint(2, 15)
    return f"{a} × {b} = ?", _num_check(a * b)


# --- Level 2: medium ---

def _fraction():
    a, b = random.randint(1, 8), random.randint(2, 9)
    c, d = random.randint(1, 8), random.randint(2, 9)
    result = Rational(a, b) + Rational(c, d)
    return f"{a}/{b} + {c}/{d} = ?", _sympy_check(result)

def _power():
    base = random.randint(2, 7)
    exp = random.randint(2, 4)
    return f"{base}^{exp} = ?", _num_check(base ** exp)

def _percentage():
    pct = random.choice([10, 15, 20, 25, 50])
    num = random.randint(2, 20) * 10
    answer = (pct * num) // 100
    return f"{pct}% of {num} = ?", _num_check(answer)

def _modulo():
    a = random.randint(20, 99)
    b = random.randint(3, 12)
    return f"{a} mod {b} = ?", _num_check(a % b)


# --- Level 3: hard ---

def _quadratic():
    a, b = random.randint(-6, 6), random.randint(-6, 6)
    while a == b:
        b = random.randint(-6, 6)
    expanded = sp.expand((x - a) * (x - b))
    roots = sorted([a, b])
    return f"solve: {expanded} = 0  (x = ?, comma separated)", _roots_check(roots)

def _derivative():
    options = [
        ("x²", 2 * x),
        ("x³", 3 * x ** 2),
        ("x² + 3x", 2 * x + 3),
        ("2x² - 5x + 1", 4 * x - 5),
        ("x³ - 2x", 3 * x ** 2 - 2),
        ("4x² + 6x - 3", 8 * x + 6),
    ]
    expr_str, deriv = random.choice(options)
    return f"d/dx [{expr_str}] = ?", _sympy_check(deriv)

def _prime_factor():
    n = random.choice([12, 18, 24, 30, 36, 48, 60, 72, 84, 96, 100, 120, 180, 210])
    return f"prime factorization of {n}  (e.g. 2^2*3)", _factor_check(n)


# --- Level 4: nightmare ---

def _integral():
    options = [
        ("∫ 2x dx", x ** 2),
        ("∫ 3x² dx", x ** 3),
        ("∫ x dx", Rational(1, 2) * x ** 2),
        ("∫ 6x² + 2x dx", 2 * x ** 3 + x ** 2),
        ("∫ 4x³ dx", x ** 4),
    ]
    q, ans = random.choice(options)
    return f"{q} = ?  (ignore +C)", _sympy_check(ans)

def _system_of_equations():
    sx, sy = random.randint(1, 5), random.randint(1, 5)
    # Retry until the coefficient matrix has a non-zero determinant (unique solution).
    # Fallback values are pre-chosen to guarantee det != 0.
    a, b, c, d = 1, 2, 3, 5
    for _ in range(50):
        a_, b_ = random.randint(1, 4), random.randint(1, 4)
        c_, d_ = random.randint(1, 4), random.randint(1, 4)
        if a_ * d_ - b_ * c_ != 0:
            a, b, c, d = a_, b_, c_, d_
            break
    r1 = a * sx + b * sy
    r2 = c * sx + d * sy
    q = f"{a}x + {b}y = {r1}\n       {c}x + {d}y = {r2}\n       x = ?, y = ?  (format: x,y)"
    return q, _system_check(sx, sy)

def _hard_derivative():
    options = [
        ("d/dx [x⁴ - 4x³ + 6x]", 4 * x ** 3 - 12 * x ** 2 + 6),
        ("d/dx [x³ - 3x² + 3x - 1]", 3 * x ** 2 - 6 * x + 3),
        ("d/dx [5x³ - 2x² + 7x]", 15 * x ** 2 - 4 * x + 7),
    ]
    q, ans = random.choice(options)
    return f"{q} = ?", _sympy_check(ans)


# --- answer checkers ---

def _num_check(expected):
    def check(raw: str) -> bool:
        try:
            return int(raw.strip()) == expected
        except (ValueError, AttributeError):
            return False
    return check

def _sympy_check(expected):
    def check(raw: str) -> bool:
        try:
            val = _safe_parse(raw)
            return sp.simplify(val - expected) == 0
        except Exception:
            return False
    return check

def _roots_check(expected: list):
    def check(raw: str) -> bool:
        try:
            parts = [p.strip().replace("x=", "").replace("x =", "") for p in raw.split(",")]
            nums = sorted(int(p) for p in parts)
            return nums == expected
        except Exception:
            return False
    return check

def _factor_check(n: int):
    def check(raw: str) -> bool:
        try:
            cleaned = (raw.strip()
                       .replace("×", "*").replace("·", "*")
                       .replace("²", "**2").replace("³", "**3").replace("⁴", "**4"))
            val = int(sp.sympify(cleaned))
            return val == n
        except Exception:
            return False
    return check

def _system_check(sx: int, sy: int):
    def check(raw: str) -> bool:
        try:
            cleaned = (raw.lower()
                       .replace("x=", "").replace("y=", "")
                       .replace("x =", "").replace("y =", "")
                       .replace(",", " "))
            nums = [int(n) for n in cleaned.split() if n]
            return len(nums) == 2 and nums[0] == sx and nums[1] == sy
        except Exception:
            return False
    return check
