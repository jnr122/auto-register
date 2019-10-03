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

    # with requests.session() as sess:

    s = requests.session()

    # get hidden tokens
    result = s.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token_1 = list(set(tree.xpath("//input[@name='RT']/@value")))[0]
    authenticity_token_2 = list(set(tree.xpath("//input[@name='ST']/@value")))[0]

    # set up payload
    payload = {
        "RT": authenticity_token_1,
        "ST": authenticity_token_2,
        "login": "yes",
        "username": USERNAME,
        "password": PASSWORD
    }


    # login attempt
    login_result = s.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

    LOGIN_URL = login_result.request.url

    str = (login_result.request.url.split("RT=")[1])
    hidden_keys = str.split(";ST=")
    payload = {
        "RT": hidden_keys[0],
        "ST": hidden_keys[1],
        "login": "yes",
        "username": USERNAME,
        "password": PASSWORD
    }

    login_result = s.post(login_result.request.url, data=payload, headers=dict(referer=LOGIN_URL))


def main():
    # constants
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

