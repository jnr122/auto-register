import requests

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
    LOGIN_URL = "https://myuvm.uvm.edu"
    result = sess.get(LOGIN_URL)

    # login attempt purely to scrape secret tokens
    login_result = sess.get(LOGIN_URL, headers=dict(referer=LOGIN_URL))
    LOGIN_URL = login_result.request.url

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
    login_result = sess.post(login_result.request.url, data=login_payload, headers=dict(referer=LOGIN_URL))
    return login_result

# skip directly to aisuvm iframe
def aisuvm_login(sess, USERNAME, PASSWORD):
    # nav links
    LOGIN_URL = "https://aisweb1.uvm.edu/pls/owa_prod/twbkwbis.P_ValLogin"
    MENU_URL = "https://aisweb1.uvm.edu/pls/owa_prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"

    # setup payload
    login_payload = {
        "sid": USERNAME,
        "PIN": PASSWORD
    }

    # TODO: clean this up, get vs post methods
    # so I look like a browser
    login_headers = {'referer' : LOGIN_URL,'user-agent' : USER_AGENT }
    menu_headers = {'referer' : MENU_URL, 'user-agent' : USER_AGENT}

    # update header dict with accepted submission format
    login_result = sess.post(LOGIN_URL, data=login_payload, headers=login_headers)

    # perform login, then get menu
    login_result = sess.post(LOGIN_URL, data=login_payload, headers=login_headers)
    login_result = sess.get(MENU_URL, headers=menu_headers)
    return login_result

# set up get request
def start_session(USERNAME, PASSWORD):
    with requests.session() as sess:
        login_result = aisuvm_login(sess, USERNAME, PASSWORD)

def main():
    LOGIN_TEXT = "login.txt"
    USERNAME, PASSWORD = get_name_pass(LOGIN_TEXT)

    start_session(USERNAME, PASSWORD)

if __name__ == '__main__':
    main()

