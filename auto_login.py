import requests
from lxml import html
from requests.exceptions import HTTPError
from urllib.parse import parse_qsl

# get password from textfile
def get_name_pass(url):
    try:
        login_file = open(url, "r")
        login = login_file.readline().split()
        PASSWORD = login[1]
        USERNAME = login[0]

        login_file.close()
        return USERNAME, PASSWORD

    except:
        return "NULL", "NULL"

# perform login
def login(sess, LOGIN_URL, USERNAME, PASSWORD):
    result = sess.get(LOGIN_URL)

    # login attempt purely to scrape secret tokensd
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


# perform add/drop
def add_drop(sess, USERNAME, PASSWORD):
    ADD_DROP_URL = "https://aisweb1.uvm.edu/pls/owa_prod/bwskfreg.P_AddDropCrse"
    # add_drop_page = sess.get(ADD_DROP_URL)
    #login_result = sess.get(ADD_DROP_URL, headers=dict(referer=ADD_DROP_URL))

    #sid = ... & PIN = ...
    login_payload = {
        "sid": "asdf",
        "PIN": "asdf"
    }

    header_payload = {'Date': 'Fri, 04 Oct 2019 14:23:11 GMT',
         'Server': 'Oracle-Application-Server-11g',
         'Content-Length': '6991',
         'Set-Cookie': 'TESTID=set, SESSID=;expires=Mon, 01-Jan-1990 08:00:00 GMT, PROXY_HASH=;expires=Mon, 01-Jan-1990 08:00:00 GMT',
         'Keep-Alive': 'timeout=15, max=99',
         'Connection': 'Keep-Alive',
         'Content-Type': 'text/html; charset=UTF-8',
         'Content-Language': 'en',
         'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    }

    #login_result = sess.post(ADD_DROP_URL, data=login_payload, headers=header_payload)
    login_result = sess.get(ADD_DROP_URL, headers=dict(referer=ADD_DROP_URL))

    print(login_result.headers)


# set up get request
def start_session(LOGIN_URL, USERNAME, PASSWORD):

    with requests.session() as sess:
        login(sess, LOGIN_URL, USERNAME, PASSWORD)



        #add_drop_page = sess.get(ADD_DROP_URL)
        add_drop(sess, USERNAME, PASSWORD)

def main():
    LOGIN_TEXT = "login.txt"
    USERNAME, PASSWORD = get_name_pass(LOGIN_TEXT)
    LOGIN_URL = "https://myuvm.uvm.edu"
    # couldn't load username/ password
    if USERNAME == "NULL" and PASSWORD == "NULL":
        print("Failed to load password")

    else:
        start_session(LOGIN_URL, USERNAME, PASSWORD)

if __name__ == '__main__':
    main()

