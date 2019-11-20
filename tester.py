from Course import Course
from Scheduler import Scheduler

def main():
    course1_options = [Course("1234","HCI","8:30 am-09:45 am", "TR"),Course("43151","Course 1","08:25 am-10:15 am", "MWF")]
    course2_options = [Course("642452","Op Sys","09:40 am-010:30 am", "p3 ")]
    course3_options = [Course("254425","ANPS","12:00 pm-12:50 pm", "MWF"), Course("75363","Course 3","12:00 pm-01:16 pm","MWF"),
                       Course("2345277","Course 3","03:00 pm-03:26 pm", "TR")]
    course4_options = [Course("857858","Sof Eng","02:20 pm-03:10 pm", "MWF"), Course("567594","Course 4","9:00 am-10:16 pm", "TR"),
                       Course("7900","Course 4","03:01 pm-04:06 pm", "MWF")]
    course5_options = [Course("76489","Lesson","11:00 am-12:00 pm", "T"), Course("453563","Course 5","3:00 am-10:16 pm", "TR"),
                       Course("000678","Course 5","03:00 pm-04:06 pm", "TR")]
    all_options = [course1_options, course2_options, course3_options,course4_options,course5_options]

    schr = Scheduler(all_options)

    print(*schr.largest_schedules, sep="\n")

main()
