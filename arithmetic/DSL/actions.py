'''
Basic actions to create list and integer tasks from.
'''

class Action():
  def __init__(self, name, input_type, output_type, function):
    self.name = name
    self.input_type = input_type
    self.output_type = output_type
    self.function = function

  def __call__(self, state, index):
    if (index is not None):
      return self.output_type(self.function(state, index))
    else:
      return self.output_type(self.function(state))

  def __str__(self):
    return self.name