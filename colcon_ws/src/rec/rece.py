
import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        # Process incoming message
        print(f"Received message from Jetson Nano: {message}")
        # Send a response if needed
        # await websocket.send("Response from Raspberry Pi")

async def start_server():
    async with websockets.serve(handle_connection, "0.0.0.0", 9000):
        print("WebSocket server started on ws://0.0.0.0:9000")
        # Keep the server running indefinitely
        await asyncio.Future()

# Run the WebSocket server
asyncio.run(start_server())
