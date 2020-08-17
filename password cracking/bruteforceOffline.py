import hashlib

def main():
    hashpass = str(input("hash: "))
    passfile = open("pass.txt",'r')

    for p in passfile.readlines():
        n = p.strip('\n')
        n = hashlib.sha1(n.encode('utf-8')).hexdigest()
        if n== hashpass:
            print("Password: {}     Hash: {}".format(p,n))
            break

if __name__ == "__main__":
    main()