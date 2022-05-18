from .actions import Action
# Can nn choose numeric values like + 1,2,3,4.... ?
# Can nn choose other parameters like size of list created in int_to_list ?

# Workaround python's reverse and sort functions to return list
def list_reverseH(l_x):
    l_x.reverse()
    return l_x

def list_sortH(l_x):
    l_x.sort()
    return l_x

# List Actions
list_p_1 = Action("list_p_1", list, list, lambda l_x: (x + 1 for x in l_x))
list_x_2 = Action("list_x_2", list, list, lambda l_x: (x**2 for x in l_x))
list_reverse = Action("list_reverse", list, list, lambda l_x: list_reverseH(l_x))
list_sort = Action("list_sort", list, list, lambda l_x: list_sortH(l_x))
list_filter = Action("list_filter", list, list, lambda l_x: (x for x in l_x if x >= 0.0))
list_sum = Action("list_sum", list, int, lambda l_x: sum(l_x))

# Integer Actions
int_add_1 = Action("int_add_1", int, int, lambda num: num + 1)
int_sub_1 = Action("int_sub_1", int, int, lambda num: num - 1)
int_mul_2 = Action("int_mul_2", int, int, lambda num: num * 2)
int_div_2 = Action("int_div_2", int, int, lambda num: num // 2)
int_to_list = Action("int_to_list", int, list, lambda num: (num for _ in range(5)))

grammar = [list_p_1, list_x_2, list_reverse, list_sort, list_filter, list_sum, int_add_1, int_sub_1, int_mul_2, int_div_2, int_to_list]

def available_actions(state):
    res = [action for action in grammar if action.input_type is type(state)]
    return res