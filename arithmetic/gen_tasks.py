import random

from . import *


def gen_tasks(n, max_length=5, max_steps=5, val_range=(-5, 5)):

  # task = [(input, seq, output)]
  tasks = []

  for i in range(n):
    # Generate that lists:
    list_len = random.randint(1, max_length)
    l_x = [random.randint(*val_range) for _ in range(list_len)]

    # Generate the action sequence
    seq_len = random.randint(1, max_steps)
    seq = random.choices(grammar, k=seq_len)

    l_y = l_x.copy()
    # print(l_y)
    # print(seq)
    for action in seq:
      l_y = (eval(action))(l_y)
    
    tasks.append((l_x, seq, l_y))
  return tasks
