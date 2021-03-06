from model import Problem, Constraint, Variable
import cProfile
import numpy as np
import time

SQUARE_SIZE = 4
NUMBER_OF_COLORS = 5

domains = []
variables = []
constraints = []

rows = [[] for i in range(SQUARE_SIZE)]

for i in range(SQUARE_SIZE):
    for j in range(SQUARE_SIZE):
        domain = list(range(NUMBER_OF_COLORS))
        v = Variable('v_' + str(i) + '_' + str(j), domain)
        variables.append(v)
        rows[i].append(v)


def get_neighbours(coordinates):
    neighbours = []
    for i in [0]:
        for j in [1]:
            x = coordinates[0] + i
            y = coordinates[1] + j
            if 0 <= x < SQUARE_SIZE and 0 <= y < SQUARE_SIZE:
                neighbours.append(rows[x][y])
    for i in [1]:
        for j in [0]:
            x = coordinates[0] + i
            y = coordinates[1] + j
            if 0 <= x < SQUARE_SIZE and 0 <= y < SQUARE_SIZE:
                neighbours.append(rows[x][y])
    return neighbours


def get_diagonal_neighbours(coordinates):
    neighbours = []
    for i in [1]:
        for j in [-1, 1]:
            x = coordinates[0] + i
            y = coordinates[1] + j
            if 0 <= x < SQUARE_SIZE and 0 <= y < SQUARE_SIZE:
                neighbours.append(rows[x][y])
    return neighbours


# for row in rows:
#     print(row)
#
# coords = (1, 1)
#
#
# print()
# print(rows[coords[0]][coords[1]])
# print(get_neighbours(coords))
# print(get_diagonal_neighbours(coords))


# binary constraints
for i, r in enumerate(rows):
    for j, v in enumerate(r):
        coords = (i, j)
        for other in get_neighbours(coords):
            constraints.append(Constraint(lambda x, y: abs(x - y) >= 2, [v, other]))
        for other in get_diagonal_neighbours(coords):
            constraints.append(Constraint(lambda x, y: abs(x - y) > 0, [v, other]))

print("Variables: ", len(variables))
print('Constraints: ', len(constraints))

p = Problem()

for v in variables:
    p.add_variable(v)

for c in constraints:
    p.add_constraint(c)

# start_time = time.time()
# solutions = p.get_all_solutions('bt')
# elapsed_time = time.time() - start_time


def solution_print(solution):
    keys = list(solution)
    coords = [(int(k.n.split('_')[1]), int(k.n.split('_')[2])) for k in keys]
    # print(coords)
    board = np.zeros(shape=(SQUARE_SIZE, SQUARE_SIZE))
    for i, k in enumerate(keys):
        board[coords[i][0], coords[i][1]] = solution[k]
    print(board)


# for s in solutions:
#     solution_print(s)
#     print()


# print('Solutions: ' + str(len(solutions)))
# print('Time: ' + str(elapsed_time))



# cProfile.run('p.get_all_solutions(\'bt\')', sort='tottime')
# cProfile.run('p.get_all_solutions(\'fc\')', sort='tottime')



# BT
print()
print('Backtracking')
bt_time = time.time()
solutions_bt, returns_number_bt, nodes_number_bt = p.get_all_solutions('bt', 'd', 'd')
bt_time = time.time() - bt_time
print('Solutions:' + str(len(solutions_bt)))
print('Time: ' + str(round(bt_time, 4)) + ' s')

# solution_bt = solutions_bt[0]

print('Nodes: ' + str(nodes_number_bt))
print('Returns: ' + str(returns_number_bt))

# FC
print()
print('Forward-checking')
fc_time = time.time()
solutions_fc, returns_number_fc, nodes_number_fc = p.get_all_solutions('fc', 'd', 'r')
fc_time = time.time() - fc_time
print('Solutions:' + str(len(solutions_fc)))
print('Time: ' + str(round(fc_time, 4)) + ' s')

# solution = solutions_fc[0]

print('Nodes: ' + str(nodes_number_fc))
print('Returns: ' + str(returns_number_fc))
