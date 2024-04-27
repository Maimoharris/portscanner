#Basic Port Scanner Developed By Maimo Harris Alias Dracula
import socket
from IPy import IP
#Here we convert domain name to IP before we scan
def convert_to_ip(host):
    try:
        main_ip=IP(host)
        return main_ip
    except ValueError:
        return socket.gethostbyname(host)
#Here is the main scanning options
def scanner(host,port):
    try:
        engine=socket.socket()
        engine.connect((host,port))
        #seting sacn time to 1 second
        engine.settimeout(1)
        ban=banner(engine).decode().strip('\n')
        try:
            print(f"Open {port} : {ban}")
        except:
            print(f"Open {port}")
    except:
        pass
#here is th option to obtain the service runing in the port
def banner(header):
    return header.recv(1024)
host=input("Enter Host Address:")
#here is where we optain all the ports in a specific range
for port in range(63535):
    convert_to_ip(host)
    scanner(host,port)
