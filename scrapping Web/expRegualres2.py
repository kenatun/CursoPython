#solo en python2
import re
import urllib
from urllib.request import urlopen

def get_li():
    code = urlopen('https://lorem2.com/')
    code = code.read()
    todo = re.findall('<li>(.+?)</lib>',code)
    for t in todo:
        if not "<a haref=" in t:
            print(t+'\n')





def main():
    get_li()


if __name__ == '__main__':
    main()