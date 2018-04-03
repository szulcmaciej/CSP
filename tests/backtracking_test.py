from model import Problem
import random
import cProfile

p = Problem()

variables = []
for i in range(7):
    p.create_and_add_variable('var' + str(i), list(range(10)))
    variables.append('var' + str(i))

functions = [
    lambda x, y: x > y,
    lambda x, y: x < y,
    lambda x, y: x == y,
    lambda x, y: x != y,
    lambda x, y: x >= y,
    lambda x, y: x <= y,
]

for i in range(7):
    operator = random.choice(functions)
    v1 = random.choice(variables)
    v2 = random.choice(variables)
    while v2 == v1:
        v2 = random.choice(variables)
    p.create_and_add_constraint(operator, [v1, v2])

print(p.variables)
print(p.constraints)
print()
print()

cProfile.run('p.get_all_solutions()', sort='tottime')
# solutions = p.get_all_solutions()

# print('Solutions:')
# for solution in solutions:
#     print(solution)