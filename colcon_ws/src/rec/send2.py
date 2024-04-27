import socket
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)  # Update with the desired IP and port
sock.connect(server_address)

try:
    while True:
        # Example values to send
        value1 = 10
        value2 = 20.5
        value3 = 'Hello from Python'

        # Send the values through the socket
        message = f'{value1},{value2},{value3}'
        sock.sendall(message.encode())
        print(f'Sent: {message}')

        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print('Exiting...')

finally:
    sock.close()
