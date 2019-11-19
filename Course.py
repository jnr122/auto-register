# Course class for keeping track of individual courses
class Course:

    # constructor
    def __init__(self, crn, title, time_range, days):
        self.crn = crn
        self.title = title
        self.time_range = time_range
        self.start_mins, self.end_mins = self.parse_time_range(time_range)
        self.days = days.split()

    # to string
    def __str__(self):
        return self.title + " " + self.time_range + " " + str(self.days)

    # check for equality
    def __eq__(self, other):
        if self.crn == other.crn:
            return True
        return False

    # allow sorting
    def __lt__(self, other):
        if self.start_mins < other.start_mins:
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
        for i in range(len(self.days)):
            if self.days[i] in other.days:
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
