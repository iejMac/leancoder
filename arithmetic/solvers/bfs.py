from arithmetic import *
from copy import copy


class Node:
  def __init__(self, s, n_prev, a_prev):
    self.s = s # state
    self.n_prev = n_prev # previous state (for returning solution)
    self.a_prev = a_prev # action taken to get to this node

  def get_path(self):
    pth = []
    n = self
    while n.n_prev is not None:
      pth.append(n.a_prev)
      n = n.n_prev
    pth.reverse()
    return pth

class BFSSolver:
  def __init__(self):
    pass

  def solve(self, x, y):
    s_0 = Node(x.copy(), None, None)
    s_T = Node(y, None, None)

    queue = [s_0]
    visited = []

    actions = grammar
    while True: # while solution not found
      # Go over queue and add next layer of nodes
      cur_queue_len = len(queue)
      for i in range(cur_queue_len):
        s_n = copy(queue[i])
        visited.append(s_n)
        
        for a in actions:
          s_np1 = Node(eval(a)(s_n.s.copy()), s_n, a)
          # Check if in terminal state
          if s_np1.s == s_T.s:
            return s_np1.get_path()
          elif s_np1 not in visited:
            queue.append(s_np1)

      queue = queue[cur_queue_len:] 
