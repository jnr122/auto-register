from Course import Course
from Scheduler import Scheduler
from functools import reduce


def main():
    num_arrays = 5

    course1_options = [Course("1234","Course 1","04:25 pm-05:15 pm"),Course("1234","Course 1","08:25 am-10:15 am")]
    course2_options = [Course("5678","Course 2","03:25 pm-04:24 pm")]
    course3_options = [Course("5678","Course 3","10:00 am-03:26 pm"), Course("5678","Course 3","12:00 pm-01:16 pm"),
                       Course("5678","Course 3","03:00 pm-03:26 pm")]
    course4_options = [Course("5678","Course 4","11:10 am-011:46 pm"), Course("5678","Course 4","9:00 am-10:16 pm"),
                       Course("5678","Course 4","04:01 pm-03:06 pm")]
    course5_options = [Course("5678","Course 5","7:10 am-08:46 am"), Course("5678","Course 5","3:00 am-10:16 pm"),
                       Course("5678","Course 5","03:00 pm-04:06 pm")]

    all_options = [course1_options, course2_options,course3_options,course4_options,course5_options]

    schedr = Scheduler(all_options)


main()
