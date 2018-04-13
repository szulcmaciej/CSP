from model import Problem, Constraint, Variable
import cProfile

SQUARE_SIZE = 4

domains = []
variables = []
constraints = []

rows = [[] for i in range(SQUARE_SIZE)]
columns = [[] for i in range(SQUARE_SIZE)]

for i in range(SQUARE_SIZE):
    for j in range(SQUARE_SIZE):
        domain = []
        for k in range(SQUARE_SIZE):
            # domain.append((i, j, k))
            domain.append(k)
        domains.append(domain)
        v = Variable('o' + str(i) + str(j), domain)
        variables.append(v)
        rows[i].append(v)
        columns[j].append(v)

# binary constraints
for r in rows:
    for i in range(len(r) - 1):
        for j in range(i + 1, len(r)):
            # constraint = Constraint(lambda x, y: x[2] != y[2], [r[i], r[j]])
            constraint = Constraint(lambda x, y: x != y, [r[i], r[j]])
            constraints.append(constraint)

for c in columns:
    for i in range(len(c) - 1):
        for j in range(i + 1, len(c)):
            # constraint = Constraint(lambda x, y: x[2] != y[2], [c[i], c[j]])
            constraint = Constraint(lambda x, y: x != y, [c[i], c[j]])
            constraints.append(constraint)


# # agregated constraints
# different3 = lambda a, b, c: len({a, b, c}) == 3
# different4 = lambda a, b, c, d: len({a, b, c, d}) == 4
# different5 = lambda a, b, c, d, e: len({a, b, c, d, e}) == 5
# different6 = lambda a, b, c, d, e, f: len({a, b, c, d, e, f}) == 6
#
# for r in rows:
#     constraint = Constraint(different4, r)
#     constraints.append(constraint)
#
# for c in columns:
#     constraint = Constraint(different4, c)
#     constraints.append(constraint)

print('Constraints: ', len(constraints))

p = Problem()

for v in variables:
    p.add_variable(v)

for c in constraints:
    p.add_constraint(c)


# cProfile.run('p.get_all_solutions(\'bt\')', sort='tottime')
# cProfile.run('p.get_all_solutions(\'fc\')', sort='tottime')



solutions_bt, returns_number_bt, nodes_number_bt = p.get_all_solutions('bt')
solutions_fc, returns_number_fc, nodes_number_fc = p.get_all_solutions('fc')


# BT
print()
print('Backtracking')
print('Solutions:' + str(len(solutions_bt)))

solution_bt = solutions_bt[0]

print('Nodes: ' + str(nodes_number_bt))
print('Returns: ' + str(returns_number_bt))

# FC
print()
print('Forward-checking')
print('Solutions:' + str(len(solutions_fc)))

solution = solutions_fc[0]

print('Nodes: ' + str(nodes_number_fc))
print('Returns: ' + str(returns_number_fc))
