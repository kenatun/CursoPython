import requests


def main():
    word = "cloudflare"
    url = requests.get("https://www.cloudflare.com/")
    cabeceras = dict(url.headers)
    verify = False
    for c in cabeceras:
        if word in cabeceras[c].lower():
            verify=True
            break
    if verify == True:
        print("Cloudflare presente")
    else:
        print("El sitio no tiene cloudflare")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n saliendo")
        exit()