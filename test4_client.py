#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    while True:
        async with websockets.connect(
                'ws://localhost:8765') as websocket:
                print("※アクションは二回までです。正しい行動をとりましょう。")
                c_name = input("名前を入力してください")
                if c_name == "":
                    print("やり直しです。何か入力してください。")
                    await hello()
                await websocket.send(c_name)

                print("目の前に自分のそっくりさんがいます！")
                c_action1 = input("どうしますか？ ")
                if c_action1 == "":
                    print("やり直しです。何か入力してください。")
                    await hello()
                await websocket.send(c_action1)
                print(f"{c_name}の行動： {c_action1}")

                s_action1 = await websocket.recv()
                print(f"そっくりさんの行動： {s_action1}！")

                c_action1 = input("次はどうしますか？ ")
                if c_action1 == "":
                    print("やり直しです。何か入力してください。")
                    await hello()
                await websocket.send(c_action1)
                print(f"{c_name}の行動： {c_action1}")

                s_action1 = await websocket.recv()
                if s_action1 == "消えた":

                    print(f"そっくりさんの行動：{s_action1}\nあなたは助かりました。")
                    break
                    asyncio.get_event_loop().close()
                else:
                    print(f"そっくりさんの行動：{s_action1}")
                    asyncio.get_event_loop()
asyncio.get_event_loop().run_until_complete(hello())
# asyncio.get_event_loop().run_forever()
