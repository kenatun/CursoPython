import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buscar", help="Opcion a buscar")
parser = parser.parse_args()



def main():
    if parser.buscar:
        bus = mechanize.Browser()
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        bus.addheaders = [('User-Agent', 'Firefox')]
        bus.open("https://www.google.com")
        
        bus.select_form(nr=0)
        bus['q'] = parser.buscar
        bus.submit()
        p = BeautifulSoup(bus.response().read(),'html5lib')
        for link in p.find_all('a'):
            u = link.get('href')
            u = u.replace('/url?q=','')
            print(u)
    else:
        print("Palabra a buscar")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()