from .actions import Action
import random

# NN will have to choose functions and parameters to the function (vals, indexes)

def list_reverseH(l_x):
    l_x.reverse()
    return l_x

def list_sortH(l_x):
    l_x.sort()
    return l_x

def list_pbH(l_x, index, val):
  curr = l_x[index]
  if (curr + val in range(-5,5)):
    l_x[index] += val
  return l_x

def list_sbH(l_x, index, val):
  curr = l_x[index]
  if (curr - val in range(-5,5)):
    l_x[index] -= val
  return l_x

# List Actions
# list_p_1 = Action("list_p_1", list, list, lambda l_x: (x + 1 for x in l_x))
# list_x_2 = Action("list_x_2", list, list, lambda l_x: (x**2 for x in l_x))
# list_reverse = Action("list_reverse", list, list, lambda l_x: list_reverseH(l_x))
# list_sort = Action("list_sort", list, list, lambda l_x: list_sortH(l_x))
# list_filter = Action("list_filter", list, list, lambda l_x: (x for x in l_x if x >= 0.0))
# list_sum = Action("list_sum", list, int, lambda l_x: sum(l_x))

# Integer Actions
# int_add_1 = Action("int_add_1", int, int, lambda num: num + 1)
# int_sub_1 = Action("int_sub_1", int, int, lambda num: num - 1)
# int_mul_2 = Action("int_mul_2", int, int, lambda num: num * 2)
# int_div_2 = Action("int_div_2", int, int, lambda num: num // 2)
# int_to_list = Action("int_to_list", int, list, lambda num: (num for _ in range(5)))

# Single value operations on list
list_pb = Action("list_pb", list, list, lambda l_x, index, val: list_pbH(l_x,index, val))
list_sb = Action("list_sb", list, list, lambda l_x, index, val: list_sbH(l_x,index, val))

grammar = [list_pb, list_sb]

def available_actions(state):
    return [action for action in grammar if action.input_type is type(state)]

# extend grammar to alter specific values in a list