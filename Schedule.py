# Scheduler class for keeping track of successful class combinations
class Schedule:
    # constructor
    def __init__(self, to_add):
        self.__to_add = to_add
        self.courses = []


        for course in to_add:
            self.add_class(course)

        self.courses.sort()

    # compare courses, currently supports compare by start time, will support other comparisons
    def __lt__(self, other):
        return self.get_earliest_start(self.courses) > other.get_earliest_start(other.courses)

    # return the earliest course start time in a list of courses
    def get_earliest_start(self, courses):
        earliest = courses[0].start_mins

        for i in range(1,len(courses)):
            if courses[i].start_mins < earliest:
                earliest = courses[i].start_mins
        return earliest


    # tostring
    def __str__(self):
        s = "num courses: " + str(len(self.courses)) + "\n"
        for course in self.courses:
            s += str(course) + "\n"

        return s

    # check for equality
    # TODO fix this, start by adding everything, figure out why duplicates still occur
    def __eq__(self, other):
        if self.get_num_courses() != other.get_num_courses():
            return False

        for i in range(self.get_num_courses()):
            if self.courses[i] not in other.get_courses():
                return False
        return True

    # add classes one by one, checking for conflicts
    def add_class(self, new_course):
        if len(self.courses) == 0:
            self.courses.append(new_course)
            return 1
        else:
            for course in self.courses:
                if course.conflicts_with(new_course):
                    return -1
            self.courses.append(new_course)
            return 1

    # getters
    def get_courses(self):
        return self.courses

    def get_num_courses(self):
        return len(self.courses)