#solo python 2 ver tecnologias

from Wappalyzer import WebPage, Wappalyzer


def main():
    wap = Wappalyzer.latest()
    try:
        web = WebPage.new_from_url("https://www.example.com")
        tecno = wap.analize(web)
        for t in tecno:
            print("Tecnologia detectada: {}".format(t))
    except:
        print("Ha ocurrido un error")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()