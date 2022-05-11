from arithmetic import gen_tasks
from arithmetic.solvers import BFSSolver

tasks = gen_tasks(5)
x, seq, y = tasks[0]

solver = BFSSolver()

sol = solver.solve(x, y)
print(x, y)
print(seq)
print(sol)
