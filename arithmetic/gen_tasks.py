import random

from . import *


def gen_tasks(n, max_length=5, max_steps=12, val_range=(-5, 5)):

  # task = [(input, seq, output)]
  tasks = []
  for i in range(n):
    # Generate that lists:
    list_len = random.randint(1, max_length)
    l_x = [random.randint(*val_range) for _ in range(list_len)]

    # Generate the action sequence
    seq_len = random.randint(1, max_steps)
    list_seq_len = random.randint(1, seq_len)
    list_seq = random.choices(list_grammar, k=list_seq_len)
    if (seq_len - list_seq_len > 0):
        list_seq[-1] = "sum_list"
    int_seq = random.choices(int_grammar, k=(seq_len - list_seq_len))

    l_y = l_x.copy()
    for action in list_seq:
      l_y = (eval(action))(l_y)
    #   print(l_y)
    
    for action in int_seq:
        l_y = (eval(action))(l_y)
    tasks.append((l_x, list_seq + int_seq, l_y))
  return tasks
