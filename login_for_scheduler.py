import requests
import constants
import re
from auto_login import read_file, get, post, aisuvm_login

# user info
USERNAME, PASSWORD = "NULL", "NULL"
CLASSES = []
TERM = ""

def main():
    global USERNAME, PASSWORD, TERM, CLASSES

    # username/ pass
    entries = read_file(constants.LOGIN_TEXT)
    USERNAME = entries[0]
    PASSWORD = entries[1]

    with requests.session() as sess: #new session

        get(sess, constants.LOGIN_CLASS_SCHEDULE, {'referer' : constants.LOGIN_CLASS_SCHEDULE, 'user-agent' : constants.USER_AGENT})

        aisuvm_login(sess, USERNAME, PASSWORD, constants.AIS_LOGIN_URL)

        get(sess, constants.CLASS_SEARCH, {'referer' : constants.ADD_CLASS_REFERER, 'user-agent' : constants.USER_AGENT})
        post(sess, constants.CLASS_SCHEDULE, {"p_calling_proc": "P_CrseSearch", "p_term":constants.TERM}, {'referer' : constants.CLASS_SCHEDULE, 'user-agent' : constants.USER_AGENT})
        classes = post(sess, constants.ALL_COURSES_LINK, constants.POST_ALL_COURSES, {'referer' : constants.ALL_COURSES_LINK, 'user-agent' : constants.USER_AGENT})

    classes_file = open("aux/schedule_page.txt","w")
    classes_file.write(classes.text)

    clean()

def clean():

    # open the text file with the raw schedule into variable raw_data
    with open("aux/schedule_page.txt", "r") as file:
        raw_data = file.read()

    rows = re.split("\n", raw_data)
    for i in range(len(rows)):
        rows_i_ = rows[i][0:4]
        if rows_i_ != "<td " and rows_i_ != "<tr>" and rows_i_ != "</tr":
            rows[i] = 'X'

    rows = [x for x in rows if x != 'X']

    all_classes = []
    for i in range(len(rows)):
        if rows[i] == "<tr>" and rows[i + 1][0:3] == "<td":
            individual_class = []
            k = 1
            while rows[i + k][0:3] == "<td":
                individual_class.append(rows[i + k])
                k += 1
            all_classes.append(individual_class)

    all_classes_clean = all_classes  # make a copy to put the clean data in (preserves the odd size of the lists)
    for i in range(len(all_classes)):
        for j in range(len(all_classes[i])):
            all_classes_clean[i][j] = re.sub('<.*?>', '', all_classes[i][j])
            if j == 0:
                if all_classes_clean[i][j] == "C" or all_classes_clean[i][j] == "&nbsp;":
                    all_classes_clean[i].append(all_classes_clean[i][j])
        if all_classes_clean[i][0] == "C" or all_classes_clean[i][0] == "&nbsp;":
            del all_classes_clean[i][0]


    return all_classes_clean



main()
clean()


