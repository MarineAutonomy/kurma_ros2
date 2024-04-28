import asyncio
import websockets

async def send_message():
    uri = "ws://192.168.0.101:9000"  # Replace with the IP address of the machine running the WebSocket server
    async with websockets.connect(uri) as websocket:
        # Send a message
        message = "Hello from client"
        await websocket.send(message)
        print(f"Sent message to server: {message}")

# Run the WebSocket client
asyncio.run(send_message())
