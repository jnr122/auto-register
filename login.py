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

# set up get request
def start_session(LOGIN_URL, URL, USERNAME, PASSWORD):

    with requests.session() as sess:

        result = sess.get(LOGIN_URL)

        # login attempt purely to scrape secret tokens
        login_result = sess.get(LOGIN_URL, headers=dict(referer=LOGIN_URL))
        LOGIN_URL = login_result.request.url

        # parse secret tokens
        str = (login_result.request.url.split("RT=")[1])
        hidden_keys = str.split(";ST=")

        # setup payload
        payload = {
            "RT": hidden_keys[0],
            "ST": hidden_keys[1],
            "login": "yes",
            "username": USERNAME,
            "password": PASSWORD
        }

        # actual login attempt
        login_result = sess.post(login_result.request.url, data=payload, headers=dict(referer=LOGIN_URL))

def main():
    LOGIN_TEXT = "login.txt"
    USERNAME, PASSWORD = get_name_pass(LOGIN_TEXT)
    LOGIN_URL = "https://myuvm.uvm.edu"
    URL = "https://myuvm.uvm.edu/web/home-community/registrar"

    # couldn't load username/ password
    if USERNAME == "NULL" and PASSWORD == "NULL":
        print("Failed to load password")

    else:
        start_session(LOGIN_URL, URL, USERNAME, PASSWORD)

if __name__ == '__main__':
    main()

