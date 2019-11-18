from Course import Course
from Schedule import Schedule
from functools import reduce

def main():
    num_arrays = 5

    course1_options = [Course("1234","Course 1","04:25 pm-05:15 pm"),Course("1234","Course 1","08:25 am-10:15 am")]
    course2_options = [Course("5678","Course 2","03:25 pm-04:24 pm")]
    course3_options = [Course("5678","Course 3","10:00 am-03:26 pm"), Course("5678","Course 3","12:00 pm-01:16 pm"),
                       Course("5678","Course 3","04:00 am-03:26 pm")]
    course4_options = [Course("5678","Course 4","11:10 am-011:46 pm"), Course("5678","Course 4","9:00 am-10:16 pm"),
                       Course("5678","Course 4","04:00 pm-03:06 pm")]
    course5_options = [Course("5678","Course 5","7:10 am-08:46 am"), Course("5678","Course 5","3:00 am-10:16 pm"),
                       Course("5678","Course 5","04:00 pm-03:06 pm")]

    all_options = [course1_options, course2_options,course3_options,course4_options,course5_options]
    # cl1 = Course("1234","Course 1","04:25 pm-05:15 pm")
    # cl2 = Course("5678","Course 3","03:25 pm-04:24 pm")
    # cl3 = Course("5678","Course 3","10:00 am-03:26 pm")

    # sch = Schedule([cl1,cl2,cl3])

    for i in range(len(course1_options)):
        for j in range(len(course2_options)):
            for k in range(len(course3_options)):
                for l in range(len(course4_options)):
                    for m in range(len(course5_options)):

                        sch = Schedule([course5_options[m], course2_options[j], course3_options[k], course4_options[l], course1_options[j]])
                        print(len(sch.get_courses()))
                        for course in sch.get_courses():
                            print(str(course))

    ranges = ((0, 3), (0, 1), (0, 3), (0, 3), (0, 3))
    from operator import mul
    operations = reduce(mul, (p[1] - p[0] for p in ranges)) - 1
    result = [i[0] for i in ranges]
    pos = len(ranges) - 1
    increments = 0
    print(result)
    while increments < operations:
        if result[pos] == ranges[pos][1] - 1:
            result[pos] = ranges[pos][0]
            pos -= 1
        else:
            result[pos] += 1
            increments += 1
            pos = len(ranges) - 1  # increment the innermost loop
            print(result)
main()