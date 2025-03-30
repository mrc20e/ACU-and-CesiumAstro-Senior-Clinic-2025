import asyncio
import websockets
import json

async def send_json(uri):
    message = {"request":"SEND_COMMAND", "command":"<COMMAND_MNEMONIC>", "paramaters":{"<param1>":'<param1_value>', "<param2>":"<param2_value>"}}
    async with websockets.connect(uri) as websocket:
        #message = str(input("Enter Message: "))
        await websocket.send(json.dumps(message, indent=4))
        print(f"Sent: {message}")

        response = await websocket.recv()
        print(f"Received: {response}")

url = "ws://localhost:8765"

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_json(url))