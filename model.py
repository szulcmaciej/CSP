import utils

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
        self.constraint_dict = {}

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

    # @staticmethod
    # def check_constraints(constraints, solution_dict):
    #     results = []
    #     # solution_variables = solution_dict.keys
    #     for c in constraints:
    #         values = [solution_dict.get(variable) for variable in c.v]
    #         results.append(c.f(*values))
    #
    #     return results

    @staticmethod
    def check_constraints(constraints, solution_dict):
        for c in constraints:
            values = [solution_dict.get(variable) for variable in c.v]
            if not c.f(*values):
                return False
        return True

    def get_solution(self, algorithm='bt'):
        result = None
        if algorithm == 'bt':
            result = self._get_solution_backtracking()
        elif algorithm == 'fc':
            result = self._get_solution_forward_checking()

        return result

    def get_all_solutions(self, algorithm='bt'):
        solutions = []
        returns_number = 0
        nodes_number = 0

        constraint_levels = self._create_constraint_levels()

        self._init_constraint_dict()
        print('constraint_dict initialized')

        if algorithm == 'bt':
            solution = {}
            solutions, returns_number, nodes_number = self._backtrack_all_solutions(solution, constraint_levels)
        elif algorithm == 'fc':
            solution = {}
            domains = [v.d for v in self.variables]
            solutions, returns_number, nodes_number = self._forward_check_all_solutions(solution, domains, constraint_levels)

        return solutions, returns_number, nodes_number

    def _get_solution_forward_checking(self):
        return []

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
            # if c.v is a subset of given variables
            if frozenset(c.v) <= vars_set:
                verified_constraints.add(c)
        return verified_constraints

    def _create_constraint_levels(self):
        constraint_levels = []
        for i in range(self.variables.__len__()):
            level = self._get_constraints_with_variables(self.variables[0:i])
            constraint_levels.append(level)
        return constraint_levels

    def _init_constraint_dict(self):
        vars_subsets = utils.subsets(self.variables)
        for subset in vars_subsets:
            self.constraint_dict[subset] = self._get_constraints_with_variables(subset)

    def _backtrack_all_solutions(self, current_solution, constraint_levels):
        valid_solutions = []
        returns_number = 0
        nodes_number = 0
        last_assigned_var_index = -1
        current_variables = []
        current_constraints = []

        # if solution dict is not empty
        if bool(current_solution):
            last_assigned_var_index = len(current_solution) - 1
            current_variables = frozenset(current_solution)
            # current_constraints = self._get_constraints_with_variables(current_variables)
            # current_constraints = constraint_levels[min(last_assigned_var_index + 1, self.variables.__len__() - 1)]
            current_constraints = self.constraint_dict[current_variables]

        # check current solution, if valid add to valid_solutions[] or go deeper (to next variable)

        # check if all constraints in current solution are met
        # if not current_solution or all(self.check_constraints(current_constraints, current_solution)):
        if not current_solution or self.check_constraints(current_constraints, current_solution):
            # if all variables are assigned, save solution, otherwise go deeper
            if set(current_variables) == set(self.variables):
                valid_solutions.append(current_solution)
            else:
                # v - variable being assigned
                v = self.variables[last_assigned_var_index + 1]
                for value in v.d:
                    solution = current_solution.copy()
                    solution[v] = value
                    valid_solutions_iter, returns_number_iter, nodes_number_iter = self._backtrack_all_solutions(solution, constraint_levels)
                    valid_solutions += valid_solutions_iter
                    returns_number += returns_number_iter
                    nodes_number += nodes_number_iter
                    nodes_number += 1
        else:
            returns_number += 1

        return valid_solutions, returns_number, nodes_number

    def _forward_check_all_solutions(self, current_solution, current_domains, constraint_levels):
        valid_solutions = []
        returns_number = 0
        nodes_number = 0
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
                    # constraints = self._get_constraints_with_variables(set(solution))
                    constraints = self.constraint_dict[frozenset(solution)]

                    # if constraints aren't met, remove current value from current_domains
                    # if constraints and not all(self.check_constraints(constraints, solution)):
                    if constraints and not self.check_constraints(constraints, solution):
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
                    valid_solutions_iter, returns_number_iter, nodes_number_iter = self._forward_check_all_solutions(solution, current_domains_copy, constraint_levels)
                    valid_solutions += valid_solutions_iter
                    returns_number += returns_number_iter
                    nodes_number += nodes_number_iter
                    nodes_number += 1
            else:
                returns_number += 1

        return valid_solutions, returns_number, nodes_number
