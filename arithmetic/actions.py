'''
Basic actions to create list tasks from. (Subject to change)
'''

def p_1(l_x):
  return [x + 1 for x in l_x]

def x_2(l_x):
  return [x**2 for x in l_x]

def reverse(l_x):
  l_x.reverse()
  return l_x

def sort(l_x):
  l_x.sort()
  return l_x

def filter(l_x):
  return [x for x in l_x if x >= 0.0]

def sum_list(l_x):
    return sum(l_x)
# integer actions
def add_1(num):
    return num + 1

def sub_1(num):
    return num - 1

def mul_2(num):
    return num * 2

def div_2(num):
    return num // 2