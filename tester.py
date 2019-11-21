from Course import Course
from Scheduler import Scheduler
import constants
import time
from login_for_scheduler import clean

def main():
    # course1_options = [Course("1234","HCI","8:30 am-09:45 am", "TR"),Course("43151","Course 1","08:25 am-10:15 am", "MWF")]
    # course2_options = [Course("642452","Op Sys","09:40 am-010:30 am", "p3 ")]
    # course3_options = [Course("254425","ANPS","12:00 pm-12:50 pm", "MWF"), Course("75363","Course 3","12:00 pm-01:16 pm","MWF"),
    #                    Course("2345277","Course 3","03:00 pm-03:26 pm", "TR")]
    # course4_options = [Course("857858","Sof Eng","02:20 pm-03:10 pm", "MWF"), Course("567594","Course 4","9:00 am-10:16 pm", "TR"),
    #                    Course("7900","Course 4","03:01 pm-04:06 pm", "MWF")]
    # course5_options = [Course("76489","Lesson","11:00 am-12:00 pm", "T"), Course("453563","Course 5","3:00 am-10:16 pm", "TR"),
    #                    Course("000678","Course 5","03:00 pm-04:06 pm", "TR")]
    # all_options = [course1_options, course2_options, course3_options,course4_options,course5_options]
    #
    # schr = Scheduler(all_options)
    #
    # print(*schr.largest_schedules, sep="\n")
    #

    # start = time.time()
    get_courses_from_text("Afd")
    # print(time.time()-start)




def get_courses_from_text(crns):

    all_courses_text = clean()
    # blank spaces precede
    with open("aux/classes.txt", "w") as file:
        for course in all_courses_text:
            file.write(str(course) + "\n")

    crns = ["10142","10670", "13865", "12781", "13925", "10637", "10385", "13813"]
    titles = ["" for crn in crns]
    all_options = [[] for crn in crns]



    for text_course in all_courses_text:
        if len(text_course) >= 18 :
            for i in range(len(crns)):
                if text_course[0] == crns[i] == crns[i]:
                    titles[i] = text_course[6]

    for i in range(len(titles)):
        all_options[i] = ([Course(text_course) for text_course in all_courses_text if len(text_course) >= 18 and text_course[6] == titles[i]])

    for options in all_options:
        print(len(options))

    schr = Scheduler(all_options)
    # print(*schr.largest_schedules, sep="\n")



main()
