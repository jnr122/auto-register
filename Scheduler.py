from functools import reduce
from operator import mul
from Schedule import Schedule
from Course import Course
from itertools import permutations
import time
import re

# Scheduler class generating and attempting to combine course permutations
class Scheduler:

    # constructor
    def __init__(self, crns):

        self.all_options = self.get_courses_from_text(crns)
        self.max_num_courses = 0
        self.largest_schedules = []

        start = time.time()
        self.generate_combinations()
        self.largest_schedules.sort()
        print(time.time() - start)

    # tostring
    def __str__(self):
        s = ""
        for sch in self.largest_schedules:
            s += str(sch) + "\n"
        return s

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

                combination = []
                for i in range(len(indices)):
                    combination.append(self.all_options[i][indices[i]])

                self.schedule_combination(combination)
                # self.generate_permutations(combination)


        else:
            # one class section for each course: unlikely
            combination = [option[0] for option in self.all_options]
            self.schedule_combination(combination)
            # self.generate_permutations(combination)

    # modified greedy algorithm
    # schedule all combinations of a given list of courses, adding unique max
    def schedule_combination(self, combination):
        # to_schedule = [[] for _ in combination]
        #
        # # check if there are any classes with equal end times
        # for i in range(len(combination)):
        #     a_course = combination[i]
        #     course_options = [a_course]
        #
        #     j = i + 1
        #     while j < len(combination):
        #         # check if they have the same end time on the same day and havent been seen before
        #         other_course = combination[j]
        #         if a_course.end_mins == other_course.end_mins and a_course.same_day_as(other_course):
        #             course_options.append(other_course)
        #         j += 1
        #         to_schedule[i] = (course_options)
        #
        #
        #
        #
        # # for tosch in to_schedule:
        # #         print (*(tosch), sep="\n")
        #
        # pr = [(x) for x in to_schedule]
        # for p in pr:
        #     print(str(p))

        sch = Schedule(combination)
        num_courses = sch.get_num_courses()
        if num_courses > self.max_num_courses:
            self.largest_schedules = []
            self.max_num_courses = num_courses
            self.add_schedule(sch)
            # self.largest_schedules.append(sch)
        elif num_courses == self.max_num_courses:
            # self.largest_schedules.append(sch)
            self.add_schedule(sch)

    # for testing against greedy algorithm modifications
    def generate_permutations(self, combination):
        for p in list(permutations(combination)):
            sch = Schedule((p))
            num_courses = sch.get_num_courses()
            if num_courses > self.max_num_courses:
                self.largest_schedules = []
                self.max_num_courses = num_courses
                self.add_schedule(sch)
            elif num_courses == self.max_num_courses:
                self.add_schedule(sch)

    # this isnt working
    def add_schedule(self, sch):
        repeat = False
        # if self.max_num_courses == 8:
        #     print("h")
        # if len(self.largest_schedules) > 1:
        #     print("jakl")
        for self_sch in self.largest_schedules:
            if sch == self_sch:
                # print("repeat")

                repeat = True
        if not repeat:
            self.largest_schedules.append(sch)

    def get_courses_from_text(self, crns):
        #TODO error handling

        all_courses_text = self.clean()
        # blank spaces precede
        with open("aux/classes.txt", "w") as file:
            for course in all_courses_text:
                file.write(str(course) + "\n")

        titles = ["" for crn in crns]
        all_options = [[] for crn in crns]

        for text_course in all_courses_text:
            if len(text_course) >= 18:
                for i in range(len(crns)):
                    if text_course[0] == crns[i] == crns[i]:
                        titles[i] = text_course[6]

        for i in range(len(titles)):
            all_options[i] = ([Course(text_course) for text_course in all_courses_text if
                               len(text_course) >= 18 and text_course[6] == titles[i]])

        return all_options

    def clean(self):

        # open the text file with the raw schedule into variable raw_data
        with open("aux/schedule_page.txt", "r") as file:
            raw_data = file.read()

        rows = re.split("\n", raw_data)
        for i in range(len(rows)):
            rows_i_ = rows[i][0:4]
            if rows_i_ != "<td " and rows_i_ != "<tr>" and rows_i_ != "</tr":
                rows[i] = 'X'

        rows = [x for x in rows if x != 'X']

        all_classes = []
        for i in range(len(rows)):
            if rows[i] == "<tr>" and rows[i + 1][0:3] == "<td":
                individual_class = []
                k = 1
                while rows[i + k][0:3] == "<td":
                    individual_class.append(rows[i + k])
                    k += 1
                all_classes.append(individual_class)

        all_classes_clean = all_classes  # make a copy to put the clean data in (preserves the odd size of the lists)
        for i in range(len(all_classes)):
            for j in range(len(all_classes[i])):
                all_classes_clean[i][j] = re.sub('<.*?>', '', all_classes[i][j])
                if j == 0:
                    if all_classes_clean[i][j] == "C" or all_classes_clean[i][j] == "&nbsp;":
                        all_classes_clean[i].append(all_classes_clean[i][j])
            if all_classes_clean[i][0] == "C" or all_classes_clean[i][0] == "&nbsp;":
                del all_classes_clean[i][0]

        return all_classes_clean

