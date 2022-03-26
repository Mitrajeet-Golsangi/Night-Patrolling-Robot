import socket, pickle, struct
import cv2

# Creation of a Socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Host IP : ", host_ip)
port = 5000
socket_address = (host_ip, port)

# Binding the socket
server_socket.bind(socket_address)

# Socket Listen

server_socket.listen(5)
print("Listening at : ", socket_address)

# Socket Accept

while True:
    client_socket, addr = server_socket.accept()
    print("Got Connection from :", addr)
    
    if client_socket:
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            img, frame = cap.read()
            a = pickle.dumps(frame)
            
            msg = struct.pack("Q", len(a)) + a
            client_socket.sendall(msg)
            
            cv2.imshow("Transimission", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

client_socket.close()