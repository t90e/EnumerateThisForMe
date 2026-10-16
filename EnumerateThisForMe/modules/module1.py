import sys, nmap

def f(domain, fullscan, headers):
    nm = nmap.PortScanner()
    if fullscan == "True":
        nm.scan(hosts=domain, arguments='-sV -sS -O -p-')
    elif headers == "True":
        nm.scan(hosts=domain, arguments='-p80,443 --script=http-headers')
    else:
        nm.scan(hosts=domain, arguments='-sV -sS -O')

    print(nm.csv())

if __name__ == "__main__":
    f(sys.argv[1], sys.argv[2], sys.argv[3])

