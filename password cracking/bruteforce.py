import hashlib
import urllib.request

def main():
    hashpass = str(input("hash: "))
    passwordlist = urllib.request.urlopen("https://gist.githubusercontent.com/TylerRockwell/e66bb76374aba34ed430dab2617e9d4a/raw/9733e873326835ed91fe63cc269d69b0cb559160/1000_common_passwords").read()
    for p in passwordlist.decode('utf8').split('\n'):
        z = hashlib.md5(p.encode('utf-8')).hexdigest()
        if  z == hashpass:
            print("Password: {}   Hash: {}".format(p,z))


if __name__ == "__main__":
    main()