from Scheduler import Scheduler

def main():

    crns = ["92751"]#, "92879"]


    schr = Scheduler(crns)
    # print(len(schr.largest_schedules))
    print(schr)


main()
