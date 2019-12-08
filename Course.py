# Course class for keeping track of individual courses
class Course:

    # constructor
    def __init__(self, course_list):

        #TODO account for time is TBA
        self.crn = course_list[0]
        self.subj = course_list[1]
        self.crse = course_list[2]
        self.sec = course_list[3]
        self.cmp = course_list[4]
        self.cred = course_list[5]
        self.title = course_list[6]
        self.days = list(course_list[7])
        self.time_range = course_list[8]
        self.start_mins, self.end_mins = self.parse_time_range(self.time_range)
        self.cap = course_list[9]
        self.act = course_list[10]
        self.rem = course_list[11]
        self.XLcap = course_list[12]
        self.XLact = course_list[13]
        self.XLrem = course_list[14]
        self.instr = course_list[15]
        self.date = course_list[16]
        self.loc = course_list[17]

        if len(course_list) > 18:
            if course_list[18] == "C":
                self.full = True
            else:
                self.full = False

    # to string
    def __str__(self):
        return self.crn + " " + self.title + " " + self.time_range + " " + str(self.days)

    # check for equality
    def __eq__(self, other):
        if self.crn == other.crn:
            return True
        return False

    # allow sorting by end time for greedy algorithm
    def __lt__(self, other):
        if self.end_mins < other.end_mins:
            return True
        return False

    # convert time string to mins since midnight
    def time_to_mins(self, time):
        try:
            hours = int(time.split(":")[0])
            mins = int(time.split(":")[1])

            return mins + hours * 60
        except:
            print("Invalid time val in time_to_mins")
            return -1

    # turn time that looks like 04:25 pm-05:15 pm into time that looks like start:
    def parse_time_range(self, time_range):
        try:
            time_mins = []
            times = time_range.split("-")

            # times containts the split start and end time
            for time in times:
                time_str = time.split(" ")
                if time_str[1] == "pm":
                    hour = time_str[0].split(":")[0]
                    if hour != "12":
                        hour = str(int(hour) + 12)

                    time_mins.append(self.time_to_mins(hour + ":" + time_str[0].split(":")[1]))
                else:
                    time_mins.append(self.time_to_mins(time_str[0]))

            return int(time_mins[0]), int(time_mins[1])
        except:
            print("Invalid time val in parse_time")
            return -1, -1

    # checks two Courses to see if there are any conflicts
    def conflicts_with(self, other):
        if self.same_day_as(other):
            # self start during other
            if other.start_mins <= self.start_mins <= other.end_mins:
                return True

            # self end during other
            elif other.start_mins <= self.end_mins <= other.end_mins:
                return True

            # other start during self
            elif self.start_mins <= other.start_mins <= self.end_mins:
                return True

            # other end during self
            elif self.start_mins <= other.end_mins <= self.end_mins:
                return True

            return False

        return False

    def same_day_as(self, other):
        for i in range(len(self.days)):
            if self.days[i] in other.days:
                return True
        return False

