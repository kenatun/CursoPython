import sys
from shodan import Shodan
from importlib import reload

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf8")
key = "zGToTmCJQ8QICf7NYkDEcoFkKI3t0QEi"

motor = Shodan(key)
try:
    query = motor.search("struts")
    print("Total de resultados: {}".format(query['total']))
    for host in query["matches"]:
        print("Ip: {}".format(host['ip_str']))
        print("Puerto: {}".format(host['port']))
        print("ORG: {}".format(host['org']))
        try:
            print("ASN: {}".format(host['asn']))
        except:
            print("Location: {}".format(host['location']))
        for l in host['location']:
            print(l + " : " + str(host['location'][l]))

        print(host['data'])
except:
    print("Error")