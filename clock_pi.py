# import math
# import sympy
# from sympy.abc import x

# print(math.sin(math.radians(270)))


# h = sympy.poly(5/3600*x)
# m = sympy.poly(1/60*x)
# s = sympy.poly(x)

# print(sympy.solve(h, m))

# print(h)


tripose = []
for t in range(3600 * 24):
    h = 5 / 3600 * t
    if h >= 60:
        h -= 60
    m = 1 / 60 * t
    if m >= 60:
        m -= 60
    s = t
    if s >= 60:
        s -= 60

    if h == m == s:
        tripose.append(t)
        print(t)
print(tripose)
