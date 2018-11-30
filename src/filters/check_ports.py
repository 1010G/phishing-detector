import socket

from contextlib import closing

def check_port(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            return True
        else:
            return False

def check(url):
    # Check for 80 
    if not check_port(url, 80) or not check_port(url, 443):
        return 1
    else:
        return 0

if __name__ == "__main__":
    print (check("google.fr"))