
import requests
from bs4 import BeautifulSoup

def main():
    a = requests.get("https://www.whois.com/whois/uncp.edu.pe")
    soup = BeautifulSoup(a.text,'html5lib')
    for l in soup.find_all("pre"):
        print(l.get_text())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n saliendo")
        exit()