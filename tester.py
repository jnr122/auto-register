from Course import Course
from Scheduler import Scheduler
from Schedule import Schedule

from functools import reduce


def main():
    num_arrays = 5

    course1_options = [Course("1234","Course 1","04:25 pm-05:15 pm", "MWF"),Course("43151","Course 1","08:25 am-10:15 am", "MWF")]
    course2_options = [Course("642452","Course 2","03:25 pm-04:24 pm", "TR")]
    course3_options = [Course("254425","Course 3","10:00 am-03:26 pm", "TR"), Course("75363","Course 3","12:00 pm-01:16 pm","MWF"),
                       Course("2345277","Course 3","03:00 pm-03:26 pm", "TR")]
    course4_options = [Course("857858","Course 4","11:10 am-011:46 pm", "MWF"), Course("567594","Course 4","9:00 am-10:16 pm", "TR"),
                       Course("7900","Course 4","03:01 pm-04:06 pm", "MWF")]
    course5_options = [Course("76489","Course 5","7:10 am-08:46 am", "MWF"), Course("453563","Course 5","3:00 am-10:16 pm", "TR"),
                       Course("000678","Course 5","03:00 pm-04:06 pm", "TR")]

    all_options = [course1_options, course2_options,course3_options,course4_options,course5_options]

    schedr = Scheduler(all_options)


main()
