from auto_login import get
import requests
import constants
from lxml import html


def start_session():
    with requests.session() as sess:
        result = get(sess, "https://giraffe.uvm.edu/~rgweb/batch/swrsectc_spring_soc_202001/all_sections.html",
                      {'referer': constants.AIS_TERM_SELECTION_URL, 'user-agent': constants.USER_AGENT})

    print(result.text.split("\n"))

def main():
    start_session()



if __name__ == '__main__':
    main()