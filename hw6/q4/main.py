import re
import sympy as sp

# === Symbol and Function Definitions ===
hbar = sp.symbols('\\hbar', real=True, positive=True)


def L_pm(j, m, p=True):
    return hbar * sp.sqrt(j * (j+1) - m*m + (-1 if p else 1) * m)


def compute(j, m1, m2):
    T1 = L_pm(j, m1, p=True) * L_pm(j, m1, p=False)
    T2 = -hbar ** 2 * m1
    T3 = L_pm(j, m2, p=True) * L_pm(j, m2, p=False)
    T4 = -hbar ** 2 * m2
    T5 = 2 * hbar ** 2 * m1 * m2
    T6 = L_pm(j, m1, p=True) * L_pm(j, m2, p=False)
    T7 = L_pm(j, m1, p=False) * L_pm(j, m2, p=True)
    return T1 + T2 + T3 + T4 + T5 + T6 + T7


# === Regex to match \ket{m1, m2}
pattern = r"\\ket\{\s*(-?\d+)\s*,\s*(-?\d+)\s*\}"

# === Replacement functions


def replacer_L2(match):
    m1, m2 = map(int, match.groups())
    expr = sp.simplify(compute(j, m1, m2))
    return f"{sp.latex(expr)}\\cdot\\ket{{{m1}, {m2}}}"


def replacer_Lz(match):
    m1, m2 = map(int, match.groups())
    expr = sp.simplify(hbar * (m1 + m2))
    return f"{sp.latex(expr)}\\cdot\\ket{{{m1}, {m2}}}"


# === File processing ===
j = 1

print(r"\begin{tabular}{|c|c|c|}")
print(r"\hline")
print(r"Original Expression & $\hat L_z$ & $\hat L^2$ \\")
print(r"\hline")

with open("vectors.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        # sanitize just in case
        original = line.replace("\\bar{\\h}", "\\hbar")
        lz = re.sub(pattern, replacer_Lz, line).replace("\\bar{\\h}", "\\hbar")
        l2 = re.sub(pattern, replacer_L2, line).replace("\\bar{\\h}", "\\hbar")
        print(f"${original}$ & ${lz}$ & ${l2}$ \\\\")
        print(r"\hline")

print(r"\end{tabular}")
