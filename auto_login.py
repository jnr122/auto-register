import requests

# globals

# nav links
AIS_LOGIN_URL = "https://aisweb1.uvm.edu/pls/owa_prod/twbkwbis.P_ValLogin"
AIS_MENU_URL = "https://aisweb1.uvm.edu/pls/owa_prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu"
AIS_TERM_SELECTION_URL = "https://aisweb1.uvm.edu/pls/owa_prod/bwskfreg.P_AltPin"

MYUVM_LOGIN_URL = "https://myuvm.uvm.edu"
# so I look like a browser
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"

# user info
LOGIN_TEXT = "login.txt"
USERNAME, PASSWORD = "NULL", "NULL"

def get(sess, url, headers):
    return sess.get(url, headers=headers)

def post(sess, url, payload, headers):
    return sess.post(url, payload, headers=headers)

# get password from textfile
def get_name_pass(url):
    try:
        login_file = open(url, "r")
        login = login_file.readline().split()
        USERNAME = login[0]
        PASSWORD = login[1]

        login_file.close()
        return USERNAME, PASSWORD

    except:
        print("Place username and password in adjacent login.txt file in format: username password")
        exit()

# perform login with hidden tokens for myuvm page
# no longer necessary, but maybe useful later
def myuvm_login(sess, USERNAME, PASSWORD):
    result = get(sess, MYUVM_LOGIN_URL, dict(referer=MYUVM_LOGIN_URL))

    # login attempt purely to scrape secret tokens
    login_result = get(sess, MYUVM_LOGIN_URL, dict(referer=MYUVM_LOGIN_URL))

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
    login_result = post(sess, login_result.request.url, login_payload, dict(referer=MYUVM_LOGIN_URL))

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
    result = post(sess, AIS_LOGIN_URL, login_payload, {'referer' : AIS_LOGIN_URL,'user-agent' : USER_AGENT })
    result = post(sess, AIS_LOGIN_URL, login_payload, {'referer' : AIS_LOGIN_URL, 'user-agent' : USER_AGENT})
    result = get(sess, AIS_MENU_URL, {'referer' : AIS_MENU_URL, 'user-agent' : USER_AGENT})

    return result

# set up get request
def start_session(USERNAME, PASSWORD):
    with requests.session() as sess:
        login_result = aisuvm_login(sess, USERNAME, PASSWORD)

        result = post(sess, AIS_TERM_SELECTION_URL, {"term_in" : 201909}, {'referer' : AIS_TERM_SELECTION_URL, 'user-agent' : USER_AGENT})


def main():
    global USER_NAME, PASSWORD
    USERNAME, PASSWORD = get_name_pass(LOGIN_TEXT)
    start_session(USERNAME, PASSWORD)

if __name__ == '__main__':
    main()

