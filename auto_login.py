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

# skip directly to aisuvm iframe
def aisuvm_login(sess, USERNAME, PASSWORD):

    # setup payload
    login_payload = {
        "sid": USERNAME,
        "PIN": PASSWORD
    }

    # update header dict with accepted submission format
    # perform login, then get menu
    result = post(sess, constants.AIS_LOGIN_URL, login_payload,
                  {'referer': constants.AIS_LOGIN_URL, 'user-agent': constants.USER_AGENT })
    result = post(sess, constants.AIS_LOGIN_URL, login_payload,
                  {'referer': constants.AIS_LOGIN_URL, 'user-agent': constants.USER_AGENT})
    result = get(sess, constants.AIS_MENU_URL,
                 {'referer' : constants.AIS_MENU_URL, 'user-agent' : constants.USER_AGENT})

    return result

# scrape existing CRNS before passing in new ones
def make_add_payload(result):
    s = "term_in=" + TERM + "&"
    s += constants.DUMMY

    # existing crns
    tree = html.fromstring(result.text)
    crns = list(set(tree.xpath("//input[@name='CRN_IN']/@value")))
    crns.remove("DUMMY")

    # loop through adding existing
    for crn in crns:
        s += "RSTS_IN=&UVM_REQ_WD_IND_IN=" + crn + "+N&assoc_term_in=" + TERM + "&CRN_IN=" + crn + "&"

    # loop through adding new
    for i in range(len(CLASSES)):
        s += "RSTS_IN=RW&CRN_IN="+CLASSES[i]+"&assoc_term_in=&start_date_in=&end_date_in=&UVM_REQ_WD_IND_IN=DUMMY&"

    # request tail
    s += "regs_row="+str(len(crns))+"&wait_row=0&add_row=10&REG_BTN=Submit+Changes"

    return s

# set up get request
def start_session(USERNAME, PASSWORD):
    with requests.session() as sess:
        login_result = aisuvm_login(sess, USERNAME, PASSWORD)

        result = post(sess, constants.AIS_TERM_SELECTION_URL, {"term_in" : TERM},
                      {'referer': constants.AIS_TERM_SELECTION_URL, 'user-agent':  constants.USER_AGENT})
        add_payload = make_add_payload(result)

        result = post(sess, constants.ADD_URL, add_payload,
                      {'referer':  constants.AIS_TERM_SELECTION_URL, 'user-agent':  constants.USER_AGENT})

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

    start_session(USERNAME, PASSWORD)

if __name__ == '__main__':
    main()

