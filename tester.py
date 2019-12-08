from Scheduler import Scheduler

def main():

    # crns = ["10142", "10670", "13865", "12781", "13925", "10637", "10385", "13813"]
    # crns = ["90594", "91685", "90595", "92677", "94526", "90923", "90234", "90564"]
    crns = ["10435", "11181", "11203", "14854", "10385", "10637", "10461", "12950", "10649", "10439"]


    schr = Scheduler(crns)
    # print(checkIfDuplicates_1(schr.largest_schedules))
    # print(len(schr.largest_schedules))
    print((schr))


main()
