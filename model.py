class Variable:
    def __init__(self, name, domain):
        self.n = name
        self.d = domain

    def __repr__(self):
        return str(self.n)

    # def __str__(self):
    #     return str(self.n) + str(self.d)


class Constraint:
    def __init__(self, con_fun, variables):
        self.f = con_fun
        # set
        self.v = variables

    def __repr__(self):
        return str(self.v)


class Problem:
    def __init__(self):
        self.variables = []
        # set
        self.constraints = set()

    def create_and_add_variable(self, name, domain):
        self.variables.append(Variable(name, domain))

    def add_variable(self, v):
        self.variables.append(v)

    def create_and_add_constraint(self, constraint_fun, variables):
        object_variables = []
        for v in variables:
            for obj_v in self.variables:
                if obj_v.n == v:
                    object_variables.append(obj_v)
        self.constraints.add(Constraint(constraint_fun, object_variables))

    def add_constraint(self, c):
        self.constraints.add(c)

    @staticmethod
    def check_constraints(constraints, solution_dict):
        results = []
        # solution_variables = solution_dict.keys
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

    def get_all_solutions(self, algorithm='bt'):
        solutions = []

        if algorithm == 'bt':
            solution = {}
            solutions = self._backtrack_all_solutions(solution)
        elif algorithm == 'fc':
            solution = {}
            domains = [v.d for v in self.variables]
            solutions = self._forward_check_all_solutions(solution, domains)

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
        # TODO change to frozenset
        vars_set = frozenset(variables)
        for c in self.constraints:
            # if c.v is a subset of given variables
            if set(c.v) <= vars_set:
                verified_constraints.add(c)
        return verified_constraints

    def _backtrack_all_solutions(self, current_solution):
        valid_solutions = []
        last_assigned_var_index = -1
        current_variables = []
        current_constraints = []

        # if solution dict is not empty
        if bool(current_solution):
            last_assigned_var_index = len(current_solution) - 1
            current_variables = set(current_solution)
            current_constraints = self._get_constraints_with_variables(current_variables)

        # check current solution, if valid add to valid_solutions[] or go deeper (to next variable)

        # check if all constraints in current solution are met
        if not current_solution or all(self.check_constraints(current_constraints, current_solution)):
            # if all variables are assigned, save solution, otherwise go deeper
            if set(current_variables) == set(self.variables):
                valid_solutions.append(current_solution)
            else:
                # v - variable being assigned
                v = self.variables[last_assigned_var_index + 1]
                for value in v.d:
                    solution = current_solution.copy()
                    solution[v] = value
                    valid_solutions = valid_solutions + self._backtrack_all_solutions(solution)

        return valid_solutions

    def _forward_check_all_solutions(self, current_solution, current_domains):
        valid_solutions = []
        last_assigned_var_index = -1
        current_variables = []

        # if solution dict is not empty
        if bool(current_solution):
            last_assigned_var_index = len(current_solution) - 1
            current_variables = set(current_solution)
        else:
            current_domains = [v.d.copy() for v in self.variables]

        # (don't) check current solution, if valid add to valid_solutions[] or go deeper (to next variable)

        # update domains for remaining variables for current solution, if any domain is empty return nothing

        # if all variables are assigned, save solution, otherwise go deeper
        if set(current_variables) == set(self.variables):
            valid_solutions.append(current_solution)
        else:
            # check domains for remaining variables
            for i in range(last_assigned_var_index + 1, len(self.variables)):
                # check every value in remaining domains
                var_domain = current_domains[i].copy()
                for v in var_domain:
                    solution = current_solution.copy()
                    solution[self.variables[i]] = v
                    constraints = self._get_constraints_with_variables(set(solution))
                    # if constraints aren't met, remove current value from current_domains
                    if constraints and not all(self.check_constraints(constraints, solution)):
                        current_domains[i].remove(v)

            # check if any of remaining domains is empty
            if min(list(map(len, current_domains))) > 0:
                # v - variable being assigned
                v = self.variables[last_assigned_var_index + 1]
                v_domain = current_domains[last_assigned_var_index + 1]
                for value in v_domain:
                    solution = current_solution.copy()
                    solution[v] = value
                    current_domains_copy = [d.copy() for d in current_domains]
                    valid_solutions = valid_solutions + self._forward_check_all_solutions(solution, current_domains_copy)

        return valid_solutions
