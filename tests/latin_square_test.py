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


print(rows)
print(columns)

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

# print(len(constraints))

p = Problem()

for v in variables:
    p.add_variable(v)

for c in constraints:
    p.add_constraint(c)

solutions = p.get_all_solutions()

# for s in solutions:
#     print(s)

print('Solutions: ' + str(len(solutions)))

# cProfile.run('p.get_all_solutions(\'bt\')', sort='tottime')
# cProfile.run('p.get_all_solutions(\'fc\')', sort='tottime')
