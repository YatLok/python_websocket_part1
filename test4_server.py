#!/usr/bin/env python

# WS server example

import asyncio
import websockets


async def hello(websocket, path):
    c_name = await websocket.recv()
    print(f"{c_name}があらわれた")
    c_action1 = await websocket.recv()
    print(f"{c_name}の取った行動：{c_action1}")

    s_action1 = f"{c_action1}！！"

    await websocket.send(s_action1)
    print(f"こちらのとった行動：{s_action1}")
    c_action1 = await websocket.recv()
    if c_action1 == "にげる" or c_action1 == "逃げる":
        s_action1 = "消えた"
        print(f"{c_name}のとった行動：{c_action1}\nこちらのとった行動：{s_action1}\n次のクライアントを待ちます")
        await websocket.send(s_action1)
    elif c_action1 != "にげる":
        s_action1 = f"{c_name}をつかまえました\n{c_name}はもう逃げられません"
        print(f"{c_name}のとった行動：{c_action1}")
        print(s_action1)
        await websocket.send(s_action1)

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
