import requests

def main():
    a= requests.get('https://ifconfig.me')
    print('IP sin proxy: {}'.format(a.text))

    proxy={
        'http':'http://201.91.82.155:3128',
        'https':'http://201.91.82.155:3128'
    }

    b = requests.get('https://ifconfig.me', proxies=proxy)
    print('IP con proxy: {}'.format(b.text))

if __name__ == "__main__":
    main()