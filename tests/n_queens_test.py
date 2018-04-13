from model import Problem, Variable, Constraint
import numpy as np
import cProfile


QUEEN_NUMBER = 9

# domain represents the row number
domains = []
for i in range(QUEEN_NUMBER):
    domain = []
    for j in range(QUEEN_NUMBER):
        domain.append((i, j))
    domains.append(domain)

variables = [Variable('q' + str(i), domains[i]) for i in range(QUEEN_NUMBER)]

constraints = set()
for i in range(QUEEN_NUMBER - 1):
    for j in range(i + 1, QUEEN_NUMBER):
        # different rows
        constraints.add(Constraint(lambda x, y: x[1] != y[1], [variables[i], variables[j]]))
        # different diagonals
        constraints.add(Constraint(lambda q1, q2: q1[0] + q1[1] != q2[0] + q2[1], [variables[i], variables[j]]))
        constraints.add(Constraint(lambda q1, q2: q1[0] - q1[1] != q2[0] - q2[1], [variables[i], variables[j]]))

p = Problem()

for v in variables:
    p.add_variable(v)

for c in constraints:
    p.add_constraint(c)

# cProfile.run('p.get_all_solutions(\'bt\')', sort='tottime')
# cProfile.run('p.get_all_solutions(\'fc\')', sort='tottime')


# print(p.variables)
# print(domains)
# print(p.constraints)

print('Variables: ' + str(len(variables)))
print('Constraints: ' + str(len(constraints)))

solutions_bt, returns_number_bt, nodes_number_bt = p.get_all_solutions('bt')
solutions_fc, returns_number_fc, nodes_number_fc = p.get_all_solutions('fc')


# BT
print()
print('Backtracking')
print('Solutions:' + str(len(solutions_bt)))
# for s in solutions:
#     print(s)

solution_bt = solutions_bt[0]

# board = np.zeros(shape=(QUEEN_NUMBER, QUEEN_NUMBER))
#
#
# # # print first solution
# # values = [solution[k] for k in solution]
# # print(values)
# # for v in values:
# #     board[v[0], v[1]] = 1
# # print(board)


print('Nodes: ' + str(nodes_number_bt))
print('Returns: ' + str(returns_number_bt))



# FC
print()
print('Forward-checking')
print('Solutions:' + str(len(solutions_fc)))
# for s in solutions:
#     print(s)

solution = solutions_fc[0]

board = np.zeros(shape=(QUEEN_NUMBER, QUEEN_NUMBER))


# # print first solution
# values = [solution[k] for k in solution]
# print(values)
# for v in values:
#     board[v[0], v[1]] = 1
# print(board)


print('Nodes: ' + str(nodes_number_fc))
print('Returns: ' + str(returns_number_fc))
