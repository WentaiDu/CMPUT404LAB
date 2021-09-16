#!/usr/bin/env python3
import socket,time, sys

# CONSTANTS
HOST = "" # Listen for all possible hosts
PORT = 8001
BUFFER_SIZE = 1024



def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip



def main():
    extern_host = "www.google.com"
    extern_port = 80
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
    
        # Set socket options, here, reuse the same bind port
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind socket to address
        proxy_start.bind((HOST, PORT))
        
        # Set to listening mode
        proxy_start.listen(1)
        
        # Continuously listen for connections
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by:", addr)
            
            # Accepted connection
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("connecting to google")
                remote_ip=get_remote_ip(extern_host)
                proxy_end.connect((remote_ip,extern_port))
                send_full_data = conn.recv(BUFFER_SIZE)
                print(f"Sending recieved data {send_full_data} to google")
                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)
                data=proxy_end.recv(BUFFER_SIZE)
                print(f"Sending recieved data {data} to client")
                conn.send(data)
            conn.close()


if __name__ == "__main__":
    main()