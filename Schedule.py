# Scheduler class for keeping track of successful class combinations
class Schedule:
    # constructor
    def __init__(self, to_add):
        self.__to_add = to_add
        self.__courses = []

        for course in to_add:
            self.add_class(course)

        self.__courses.sort()

    # tostring
    def __str__(self):
        s = "num courses: " + str(len(self.__courses)) + "\n"
        for course in self.__courses:
            s += str(course) + "\n"

        return s

    # check for equality
    def __eq__(self, other):
        if self.get_num_courses() != other.get_num_courses():
            return False
        for i in range(self.get_num_courses()):
            if self.__courses[i] != other.get_courses()[i]:
                return False
        return True

    # add classes one by one, checking for conflicts
    def add_class(self, new_course):
        if len(self.__courses) == 0:
            self.__courses.append(new_course)
            return 1
        else:
            for course in self.__courses:
                if course.conflicts_with(new_course):
                    return -1
            self.__courses.append(new_course)
            return 1

    # getters
    def get_courses(self):
        return self.__courses

    def get_num_courses(self):
        return len(self.__courses)