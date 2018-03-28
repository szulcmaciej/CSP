# fun_a = lambda x, y: x+y
# fun_b = lambda x, y: x*y
# fun_c = lambda x, y: x/y
# fun_d = lambda x, y: x-y
#
#
# operators = [fun_a, fun_b, fun_c, fun_d]
#
# args = (3, 5)
#
# def get_results(args, operators):
#     result = [operator(*args) for operator in operators]
#     return result
#
# print(get_results(args, operators))


# from model import Problem
#
# p = Problem()
#
# p.add_variable('a', [1, 2, 3])
# p.add_variable('b', [1, 2, 3, 4, 5])
# p.add_variable('c', [3, 4, 5])
# p.add_variable('d', [1, 5, 10])
#
# p.add_constraint(lambda x, y: x < y, ('a', 'b'))
# p.add_constraint(lambda x, y: x < y, ('b', 'c'))
# p.add_constraint(lambda x, y: x < y, ('c', 'd'))
# p.add_constraint(lambda x, y, z: x < y < z, ('a', 'c', 'd'))
#
# # print(p.variables)
# # print(p.constraints)
# #
# # example = {'a': 3, 'b': 4, 'c': 5, 'd': 10}
# #
# # result = p.checkConstraints(example)
# # print(result)
# #
# solution = p.get_solution()
# print(solution)


from model import Variable

v1 = Variable('a', {1, 2, 3})
v2 = Variable('b', {1, 2, 3})

d = {v1:5, v2:7}

print(d)
