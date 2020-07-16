import urllib.request
import json


def main():
    url= "https://ipinfo.io/52.86.221.103/json"
    v = urllib.request.urlopen(url)
    j = json.loads(v.read())

    for dato in j:
        print(dato + " : " + j[dato])




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n saliendo")
        exit()