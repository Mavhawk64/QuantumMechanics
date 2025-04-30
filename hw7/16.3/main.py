import sympy as sp

a = sp.Symbol("\\hat a", commutative=False)
b = sp.Symbol("\\hat a^\\dagger", commutative=False)
I = sp.Symbol("\\mathbb I_2", commutative=True)

exp = sp.expand((a + b) ** 4, locals={"\\hat a": a, "\\hat a^\\dagger": b})

old = None
while exp != old:
    old = exp
    exp = exp.subs({a * b: I + b * a})
    exp = sp.simplify(exp)


print(sp.latex(exp))
