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
