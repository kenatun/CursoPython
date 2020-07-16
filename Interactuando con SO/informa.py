from subprocess import check_output
import subprocess

jaja = check_output('systeminfo', stderr=subprocess.STDOUT)
n=open('test.txt','wb')
n.write(jaja)
print("Cuaaaack :)")
n.close()