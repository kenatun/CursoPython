import urllib.request

def main():
    
    
    p = urllib.request.urlopen('https://ifconfig.me')
    print('Ip sin proxy: {}'.format(p.read()))

    urllib.request.install_opener(
        urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {
                    'http':'http://201.91.82.155:3128',
                    'https':'http://201.91.82.155:3128'
                }
            )
        )
    )

    peticion = urllib.request.urlopen('https://ifconfig.me')
    print("Ip con Proxy: {}".format(peticion.read()))

if __name__ == '__main__':
    main()