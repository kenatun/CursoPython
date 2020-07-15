import dns.resolver

def main():
    consultas 
    try:
        a = dns.resolver.query("google.com","MX")
        for q in a:
            print(q)
    except:
        print("No pude obtener la consulta")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n saliendo")
        exit()