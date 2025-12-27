import sys
import socket
import threading

if len(sys.argv)!=3:
    print("Input should be in the following order: py scanner.py START_PORT END_PORT")
    sys.exit()

target = "127.0.0.1"

# try:
#     target = socket.gethostbyname(sys.argv[1])
# except socket.gaierror():
#     print("Please enter correct target name or address")
#     sys.exit()

start_port = int(sys.argv[1])
end_port = int(sys.argv[2])

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((target, port))
    if not conn:
        print(f"Port {port} is open")
    s.close()

threads = []

for port in range(start_port, end_port+1):
    thread = threading.Thread(target = port_scan, args = (port,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
