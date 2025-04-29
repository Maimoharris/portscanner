# Multithreaded Port Scanner by Maimo Harris Alias Dracula
import socket
from IPy import IP
from concurrent.futures import ThreadPoolExecutor
import argparse
# Convert domain or IP string to proper IP address
def convert_to_ip(host):
    try:
        return IP(host)
    except ValueError:
        return socket.gethostbyname(host)
# Attempt to receive banner from open port
def banner(sock):
    try:
        return sock.recv(1024).decode().strip()
    except:
        return ""
# Function to scan a single port
def scanner(host, port):
    try:
        engine = socket.socket()
        engine.settimeout(1)
        engine.connect((host, port))
        ban = banner(engine)
        print(f"[+] Open {port} : {ban}" if ban else f"[+] Open {port}")
        engine.close()
    except:
        pass

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner by Maimo Harris Alias Dracula")
    parser.add_argument('--host', required=True, help='Target IP address or domain')
    parser.add_argument('--start-port', type=int, default=1, help='Start of port range (default: 1)')
    parser.add_argument('--end-port', type=int, default=65534, help='End of port range (default: 65534)')
    parser.add_argument('--threads', type=int, default=100, help='Number of threads to use (default: 100)')

    args = parser.parse_args()
    # Resolve host to IP
    target = convert_to_ip(args.host)
    print(f"\n[!] Scanning {target} from port {args.start_port} to {args.end_port} using {args.threads} threads...\n")
    # Use a ThreadPoolExecutor to scan ports concurrently
    with ThreadPoolExecutor(args.threads) as executor:
        for port in range(args.start_port, args.end_port + 1):
            executor.submit(scanner, target, port)
# Entry point
if __name__ == "__main__":
    main()
