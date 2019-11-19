import requests
import constants
from lxml import html
from auto_login import read_file
from auto_login import get
from auto_login import post


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

    # term/ classes
    entries = read_file(constants.CLASSES_TEXT)
    TERM = entries[0]
    CLASSES = entries[1:]

    with requests.session() as schedule_session: #new session
        # login_results = aisuvm_login(schedule_session,USERNAME, PASSWORD) # login at myUVM
        # # #print(login_results.text)
        add_class_results = get(schedule_session,constants.LOGIN_CLASS_SCHEDULE,{'referer' : constants.LOGIN_CLASS_SCHEDULE, 'user-agent' : constants.USER_AGENT})

        # setup payload
        login_payload = {
            "sid": USERNAME,
            "PIN": PASSWORD
        }

        # update header dict with accepted submission format
        # perform login, then get menu
        result = post(schedule_session, constants.AIS_LOGIN_URL, login_payload,
                      {'referer': constants.AIS_LOGIN_URL, 'user-agent': constants.USER_AGENT})

        add_class_results = get(schedule_session,constants.CLASS_SEARCH,{'referer' :"https://myuvm.uvm.edu/web/home-community/registrar?p_p_id=56_INSTANCE_UHUqm6dYpw1z&p_p_lifecycle=0&p_p_state=maximized&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=3&link_id=19", 'user-agent' : constants.USER_AGENT})
        add_class_results = post(schedule_session,constants.CLASS_SCHEDULE,{"p_calling_proc":"P_CrseSearch","p_term":TERM},{'referer' : constants.CLASS_SCHEDULE, 'user-agent' : constants.USER_AGENT})
        add_class_results = post(schedule_session,constants.ALL_COURSES_LINK,constants.POST_ALL_COURSES,{'referer' : constants.ALL_COURSES_LINK, 'user-agent' : constants.USER_AGENT})


main()


