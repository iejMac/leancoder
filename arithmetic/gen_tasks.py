import random

from arithmetic.DSL.grammar import available_actions

from . import *


def gen_tasks(n, max_length=5, max_steps=12, val_range=(-5, 5)):

  # task = [(input, seq, output)]
  tasks = []
  for i in range(n):
    # Generate that lists:
    list_len = random.randint(1, max_length)
    l_x = [random.randint(*val_range) for _ in range(list_len)]
    l_y = l_x.copy()
    # Generate the action sequence
    seq_len = random.randint(1, max_steps)
    seq = []
    for _ in range(seq_len):
        possible_actions = available_actions(l_y)
        action = random.choice(possible_actions)
        l_y = action(l_y)
        seq.append(action)

    tasks.append((l_x, seq, l_y))
  return tasks

# Randomly generated outputs
def gen_random(n, max_length=5, max_steps=3, val_range=(-5,5)):
  tasks = []
  for i in range(n):
    list_len = random.randint(1, max_length)
    l_x = [random.randint(*val_range) for _ in range(list_len)]
    new_list = []
    for i in range(list_len):
      new_list.append(random.randint(-5,5))

    l_y = new_list
    tasks.append((l_x, "random", l_y))

  return tasks