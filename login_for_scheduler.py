import requests
import constants
from lxml import html

# user info
USERNAME, PASSWORD = "NULL", "NULL"
CLASSES = []
TERM = ""

def get(sess, url, headers):
    return sess.get(url, headers=headers)

def post(sess, url, payload, headers):
    return sess.post(url, payload, headers=headers)

# get data from textfile
def read_file(url):
    entries = []
    try:
        file = open(url, "r")

        for line in file:
            entries.append(line.rstrip())

        file.close()
        return entries

    except:
        print("Place username and password in adjacent login.txt file in format: username password")
        exit()


# perform login with hidden tokens for myuvm page
# no longer necessary, but maybe useful later
def myuvm_login(sess, USERNAME, PASSWORD):
    result = get(sess, constants.MYUVM_LOGIN_URL, dict(referer=constants.MYUVM_LOGIN_URL))

    # login attempt purely to scrape secret tokens
    login_result = get(sess, constants.MYUVM_LOGIN_URL, dict(referer=constants.MYUVM_LOGIN_URL))

    # parse secret tokens
    str = (login_result.request.url.split("RT=")[1])
    hidden_keys = str.split(";ST=")

    # setup payload
    login_payload = {
        "RT": hidden_keys[0],
        "ST": hidden_keys[1],
        "login": "yes",
        "username": USERNAME,
        "password": PASSWORD
    }

    # actual login attempt
    login_result = post(sess, login_result.request.url, login_payload, dict(referer=constants.MYUVM_LOGIN_URL))

    return login_result


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
        login_results = myuvm_login(schedule_session,USERNAME, PASSWORD) # login at myUVM
        #print(login_results.text)
        add_class_results = get(schedule_session,constants.CLASS_SCHEDULE,{'referer' : constants.CLASS_SCHEDULE, 'user-agent' : constants.USER_AGENT})
        print(add_class_results.text)


main()


