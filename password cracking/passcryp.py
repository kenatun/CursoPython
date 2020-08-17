import hashlib

def main():
    passw = str(input("palabra: ")).encode('utf-8')

    md5pass = hashlib.md5(passw).hexdigest()
    print("MD5="+ md5pass)

    sha1pass= hashlib.sha1(passw).hexdigest()
    print("SHA1="+ sha1pass)

    sha224pass= hashlib.sha224(passw).hexdigest()
    print("SHA224="+ sha224pass)

    sha256pass= hashlib.sha256(passw).hexdigest()
    print("SHA256="+ sha256pass)

    

if __name__ == "__main__":
    main()