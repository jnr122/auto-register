from functools import reduce
from operator import mul
from itertools import permutations
from Schedule import Schedule
import time

# Scheduler class generating and attempting to combine course permutations
class Scheduler:

    # constructor
    def __init__(self, all_options):
        self.all_options = all_options
        self.max_num_courses = 0
        self.largest_schedules = []

        start = time.time()
        self.generate_combinations()
        self.largest_schedules.sort()
        print(time.time() - start)

    # generate all combinations, chose to do iteratively instead of recursively
    def generate_combinations(self):
        # store ranges to iterate over, and initialize indices
        ranges = [len(option) for option in self.all_options]
        indices = [0 for _ in ranges]

        # calculate total number of iterations
        ops = reduce(mul, ranges) - 1
        pos = len(ranges) - 1
        incr = 0
        if ops > 0:
            while incr < ops:
                if indices[pos] == ranges[pos] - 1:
                    indices[pos] = 0
                    pos -= 1
                else:
                    indices[pos] += 1
                    incr += 1
                    pos = len(ranges) - 1

                combination = [option[indices[self.all_options.index(option)]] for option in self.all_options]
                self.generate_permutations(combination)

        else:
            # one class section for each course: unlikely
            combination = [option[0] for option in self.all_options]
            self.generate_permutations(combination)

    # schedule all combinations of a given list of courses, adding unique max
    def generate_permutations(self, combination):
        for p in list(permutations(combination)):
            sch = Schedule((p))
            num_courses = sch.get_num_courses()
            if num_courses > self.max_num_courses:
                self.largest_schedules = []
                self.max_num_courses = num_courses
                self.largest_schedules.append(sch)
            elif num_courses == self.max_num_courses:
                if sch not in self.largest_schedules:
                    self.largest_schedules.append(sch)