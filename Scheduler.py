from functools import reduce
from operator import mul
from itertools import permutations
from Schedule import Schedule

# Scheduler class generating and attempting to combine course permutations
class Scheduler:

    # constructor
    def __init__(self, all_options):
        self.all_options = all_options
        self.max_num_courses = 0
        self.max_list_courses = []

        self.generate_combinations()
        print(str(self.max_list_courses[0]))


    # generate all combinations, chose to do iteratively instead of recursively
    def generate_combinations(self):
        # store ranges to iterate over
        ranges = []

        for i in range(len(self.all_options)):
            ranges.append([0, len(self.all_options[i])])

        # calculate total number of iterations
        operations = reduce(mul, (p[1] - p[0] for p in ranges)) - 1
        result = [i[0] for i in ranges]
        pos = len(ranges) - 1
        increments = 0
        while increments < operations:
            if result[pos] == ranges[pos][1] - 1:
                result[pos] = ranges[pos][0]
                pos -= 1
            else:
                combination = []
                result[pos] += 1
                increments += 1
                pos = len(ranges) - 1  # increment the innermost loop
                for n in range(len(self.all_options)):
                    combination.append(self.all_options[n][result[n]])
                self.generate_permutations(combination)

    def generate_permutations(self, combination):
        for p in list(permutations(combination)):
            sch = Schedule((p))
            num_courses = sch.get_num_courses()
            if num_courses > self.max_num_courses:
                self.max_list_courses = []
                self.max_num_courses = num_courses
                self.max_list_courses.append(sch)
            elif num_courses == self.max_num_courses:
                self.max_list_courses.append(sch)

