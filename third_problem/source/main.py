from SAT_solutions import exhaustive_enumeration, DPLL

n, m = 4, 3
c = ["1 2 3", "-1 -2 4", "2 -3 -4"]

print(exhaustive_enumeration(n, m, c))
print(DPLL(n,m,c))