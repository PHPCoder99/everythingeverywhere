# import sympy as sp
#
# # Define symbols
# q, p, Q, P = sp.symbols('q p Q P')
#
# # Define the transformation equations (example)
# A = 2
# Q = -p
# P = q+A*p**2
#
# # Define the generating function (example)
# F = sp.Function('F')(q, P)
#
# # Compute the total differential
# dF = sp.diff(F, q) * sp.diff(q, q) + sp.diff(F, P) * sp.diff(P, q)
#
# # Check for exact differentials
# exact_differential = sp.diff(dF, q) - sp.diff(dF, P)
#
# print(exact_differential)
#
# # Solve for the generating function
# generating_function = sp.solve(exact_differential, F)
# print(generating_function)

print(16/6)
print(2+3+3+3+3+2)