import requests
import constants
from auto_login import read_file, get, post


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

    with requests.session() as schedule_session: #new session
        # login_results = aisuvm_login(schedule_session,USERNAME, PASSWORD) # login at myUVM
        # # #print(login_results.text)
        add_class_results = get(schedule_session, constants.LOGIN_CLASS_SCHEDULE, {'referer' : constants.LOGIN_CLASS_SCHEDULE, 'user-agent' : constants.USER_AGENT})

        # setup payload
        login_payload = {
            "sid": USERNAME,
            "PIN": PASSWORD
        }

        # update header dict with accepted submission format
        # perform login, then get menu
        post(schedule_session, constants.AIS_LOGIN_URL, login_payload,
             {'referer': constants.AIS_LOGIN_URL, 'user-agent': constants.USER_AGENT})

        get(schedule_session, constants.CLASS_SEARCH, {'referer' : constants.ADD_CLASS_REFERER, 'user-agent' : constants.USER_AGENT})
        post(schedule_session, constants.CLASS_SCHEDULE, {"p_calling_proc": "P_CrseSearch", "p_term":TERM}, {'referer' : constants.CLASS_SCHEDULE, 'user-agent' : constants.USER_AGENT})
        classes = post(schedule_session, constants.ALL_COURSES_LINK, constants.POST_ALL_COURSES, {'referer' : constants.ALL_COURSES_LINK, 'user-agent' : constants.USER_AGENT})
        classes_file = open("aux/schedule_page.txt","w")
        classes_file.write(classes.text)

main()


