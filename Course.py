class Course:

    # constructor
    def __init__(self, crn, title, time_range):
        self.crn = crn
        self.title = title
        self.start_mins, self.end_mins = self.parse_time_range(time_range)

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
                if time.split(" ")[1] == "pm":
                    hour = time.split(" ")[0].split(":")[0]
                    (hour) = str(int(hour) + 12)

                    time_mins.append(self.time_to_mins(hour + ":" + time.split(" ")[0].split(":")[1]))
                else:
                    time_mins.append(self.time_to_mins(time.split(" ")[0]))

            return int(time_mins[0]), int(time_mins[1])
        except:
            print("Invalid time val in parse_time")
            return -1, -1

    # checks two Courses to see if there are any conflicts
    def conflicts_with(self, other):
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
