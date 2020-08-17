import requests

def main():
    a = requests.get('https://ifconfig.me')
    print('Peticion sin socks: {}'.format(a.text))

    proxy = {
        'http':'socks5://166.62.85.161:29599',
        'https':'socks5://166.62.85.161:29599'
    }

    b = requests.get('https://ifconfig.me', proxies=proxy)
    print('Ip con sock: {}'.format(b.text))

if __name__ == "__main__":
    main()