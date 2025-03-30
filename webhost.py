import websockets
import asyncio
import json

async def handler(websocket):
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            #message = json.loads(message)
            print(f"Received message: {message}")
            await websocket.send(f"Message Received")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client connection closed: {e.code} - {e.reason}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped")