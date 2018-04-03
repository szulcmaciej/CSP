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




from model import Problem

p = Problem()

p.create_and_add_variable('a', [1, 2, 3, 4, 5])
p.create_and_add_variable('b', [1, 2, 3, 4, 5])
p.create_and_add_variable('c', [1, 2, 3, 4, 5])
p.create_and_add_variable('d', [1, 2, 3, 4, 5])
p.create_and_add_variable('e', [1, 2, 3, 4, 5])

p.create_and_add_constraint(lambda x, y: x == y, ['a', 'b'])
p.create_and_add_constraint(lambda x, y: x > y, ['b', 'c'])
p.create_and_add_constraint(lambda x, y: x < y, ['d', 'e'])
p.create_and_add_constraint(lambda x, y: x < y, ['a', 'd'])
p.create_and_add_constraint(lambda x, y: x > y, ['a', 'c'])


# p.add_constraint(lambda x, y: x < y, ('c', 'd'))
# p.add_constraint(lambda x, y, z: x < y < z, ('a', 'c', 'd'))

# print(p.variables)
# print(p.constraints)
#
# example = {'a': 3, 'b': 4, 'c': 5, 'd': 10}
#
# result = p.checkConstraints(example)
# print(result)



solutions = p.get_all_solutions()
# print(solutions)

for s in solutions:
    for v in s:
        print(v, s[v], end='  ')
    print()



# fff = 'lambda x, y: x > y'
#
# f = eval(fff)
#
# print(f(2,1))





# # a = {'a':1, 'b':2}
# a = set()
# print(set(a))
#
# if a:
#     print('jest')



# from model import Variable
#
# v1 = Variable('a', {1, 2, 3})
# v2 = Variable('b', {1, 2, 3})
# v3 = Variable('c', {1, 2, 3})
#
# d = {v1:5, v2:7}
#
# d[v3] = 9
#
# print(d)
#
# a = []
#
# print(len(a) == 0 or min(a))
