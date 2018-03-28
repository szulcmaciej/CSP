class Variable:
    def __init__(self, name, domain):
        self.n = name
        self.d = domain


class Constraint:
    def __init__(self, con_fun, variable_set):
        self.f = con_fun
        # set
        self.v = variable_set


class Problem:
    def __init__(self):
        self.variables = []
        # set
        self.constraints = []

    def add_variable(self, name, domain):
        self.variables.append(Variable(name, domain))

    def add_constraint(self, constraint_fun, variables):
        self.constraints.append(Constraint(constraint_fun, variables))

    def check_constraints(self, constraints, solution_dict):
        results = []
        solution_variables = solution_dict.keys
        for c in constraints:
            values = [solution_dict.get(variable) for variable in c.v]
            results.append(c.f(*values))

        return results

    def get_solution(self, algorithm='backtracking'):
        result = None
        if algorithm == 'backtracking':
            result = self._get_solution_backtracking()
        elif algorithm == 'forward_checking':
            result = self._get_solution_forward_checking()

        return result

    def get_all_solutions(self, algorithm='backtracking'):
        # TODO
        solutions = []

        return solutions

    # def getSolutionBacktracking(self):
    #     domain_indices = [0 for v in self.variables]
    #
    #     solution = dict([(variable[0], variable[1][domain_indices[index]]) for index, variable in enumerate(self.variables)])
    #     last_increased_index = 0;
    #     print(solution)
    #
    #     while min(self.checkConstraints(solution)) is not True and last_increased_index >= 0:
    #         last_increased_index = self.changeValuesBacktracking(last_increased_index, domain_indices)
    #         solution = dict([(variable[0], variable[1][domain_indices[index]]) for index, variable in enumerate(self.variables)])
    #         print(solution)
    #
    #     return solution
    #
    def _get_solution_forward_checking(self):
        return []
    #
    # def changeValuesBacktracking(self, last_increased_index, current_indices):
    #     domain_lenghts = [len(variable[1]) for variable in self.variables]
    #
    #
    #
    #     return last_increased_index

    def _get_solution_backtracking(self):
        assigned_variables = []
        assigned_constraints = []

        assigned_variables.append(self.variables[0])
        last_assigned_variable = 0



        return []

    def _get_constraints_with_variables(self, variables):
        verified_constraints = set()
        vars_set = frozenset(variables)
        for c in self.constraints:
            if c.v in vars_set:
                verified_constraints.add(c)
        return verified_constraints

    def _backtrack_all(self, solution, var_index, domain_index):

        if domain_index + 1 < len(self.variables[var_index].d):
            # TODO check constraints
            current_variables = solution.keys
            current_constraints = self._get_constraints_with_variables(current_variables)

        else:



