from arithmetic.DSL.grammar import available_actions
from copy import deepcopy


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
    s_0 = Node(deepcopy(x), None, None)
    s_T = Node(y, None, None)

    queue = [s_0]
    visited = []
    if (x == y): return []

    while True: # while solution not found
      # Go over queue and add next layer of nodes
      cur_queue_len = len(queue)
      for i in range(cur_queue_len):
        s_n = deepcopy(queue[i])
        visited.append(s_n)
        # stop early
        if (len(visited) == 20000):
          print(f"Checked {len(visited)} programs")
          return []
        actions = available_actions(s_n.s)
        for a in actions:
          if (a.name[-1] == "b"):
            for index in range(0, len(s_n.s)):
              s_np1 = Node(a(deepcopy(s_n.s), index), s_n, a)
              # Check if in terminal state
              if s_np1.s == s_T.s:
                return s_np1.get_path()
              elif s_np1 not in visited:
                queue.append(s_np1)
          else:
            s_np1 = Node(a(s_n.s, None), s_n, a)
            # Check if in terminal state
            if s_np1.s == s_T.s:
              return s_np1.get_path()
            elif s_np1 not in visited:
              queue.append(s_np1)

      queue = queue[cur_queue_len:] 
