import socket
import ssl

if __name__ == "__main__":
    

    c = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("122.51.67.162",4433))

    cs = c.wrap_socket(s,server_hostname="122.51.67.162")
    
    a = cs.recv(4)

    print(a)
    


    

