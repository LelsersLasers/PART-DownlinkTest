import socket
import time

UDP_IP = "192.168.1.21"  # target IP address
UDP_PORT = 5005       # target port
# MESSAGE = "Hello, World!"  # message to send as bytes

print(f"UDP target IP: {UDP_IP}")
print(f"UDP target port: {UDP_PORT}")
# print(f"message: {MESSAGE}")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the UDP packet
# sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# # Close the socket
# sock.close()

try:
	i = 0
	while True:
		if i > 255:
			i = 0
		i += 1
		MESSAGE = bytes([i] * 10)
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

		time.sleep(1)  # wait for 1 second before sending the next packet
except KeyboardInterrupt:
	print("Program terminated by user.")
