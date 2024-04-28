import socket
import asyncio
import time

async def send_messages():
    # Replace with the IP address and port of the server
    server_address = ('192.168.0.101', 9000)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to {} port {}'.format(*server_address))

    try:
        # Connect to the server
        await asyncio.get_event_loop().sock_connect(sock, server_address)

        while True:
            # Send a message
            message = b"Hello from client"
            print('Sending:', message)
            sock.sendall(message)

            # Wait for a short duration before sending the next message
            await asyncio.sleep(5)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to close the connection gracefully
        pass

    finally:
        # Clean up the connection
        print('Closing socket')
        sock.close()

# Run the client
asyncio.run(send_messages())
