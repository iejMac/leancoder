from arithmetic import gen_tasks, gen_random
from arithmetic.solvers import BFSSolver
import sys
from copy import deepcopy

sys.setrecursionlimit(5000)
solver = BFSSolver()
# tasks = gen_tasks(5)
# x, seq, y = tasks[0]

# sol = solver.solve(x, y)
# print(x, y)
# print(*seq)
# print(*sol)

tasks = gen_random(5)
x, seq, y = tasks[0]
print(x,y)
sol = solver.solve(x,y)
print(*sol)
