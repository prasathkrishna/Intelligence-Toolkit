import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-.-] New Scan [-.-]')
    print('[-> Scanning IP/Website]: ' + str(target))

    a = int(input('Enter beginning range: '))
    a1 = int(input('Enter end range: '))
    b = a1 + 1

    for port in range(a, b):
        scan_port(converted_ip, port)

def get_banner(s):
    return s.recv(1024)

def check_ip(ip):
    try:
        IP(ip)
        return
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) #scan ports faster, less accurate
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[-->] Open Port ' + str(port) + ' : ' + str(banner))
        except:
            print('[-->] Open Port ' + str(port) + ' : Banner Unavailable')
    except:
        #print('[-->] Port ' + str(port) + ' is Unavailable')
        pass  #activate this line and hashtag the line above to only show open ports

print('-----')
print('Enter Comma(,) to key in multiple targets')
targets = input('[-->] Enter IP(s) or Website(s) to Scan: ')
if ',' in targets: #if there are multiple targets
    for ip_add in targets.split(','):
        scan(ip_add.strip(' ')) #strip works to remove the element stated in ' '

else:
    scan(targets)

print('[T.T] End of Scan')