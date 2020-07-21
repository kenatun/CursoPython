
def main():
    web = open('web.html',encoding="utf8")
    ini = '<p>'
    fin = '</link>'
    for l in web.readlines():
        if ini in l:
            if not "a href=" in l:
                inicio=l.find(ini)
                inicio = inicio + len(ini)
                final = l.find(fin)
                print(l[inicio:final])



if __name__ == '__main__':
    main()