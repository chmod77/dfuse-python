import asyncio
import websockets
import json

KEY = "eyJhbGciOiJLTVNFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDQ4MjczMzIsImp0aSI6Ijg5MWE2ZjcxLWYxMmUtNGY1NC04NjAzLTNjMjkyMmFlMDY1YSIsImlhdCI6MTU0MjIzNTMzMiwiaXNzIjoiZGZ1c2UuaW8iLCJzdWIiOiJDaVFBNmNieWU0SzE5Z3Q4NkFicUtRbmpKYVdTTXg0dkR3U09zZlBYUFpWQmlWSzlsTXNTUGdBL0NMUnR0L211eUE5MEFUaHZrUkR0d0RYUjhpdVBHTUlyKzFqdWprZGNZVTdPb1BSQ0hab0MvM3BLVmJkV1UwMVVvVGRMU3NDdlFaSkdreU5RIiwidGllciI6ImJldGEtdjEiLCJ2IjoxfQ.xdQq2R1wyipNeSDT-UA2CTNkzHQAshobsIB-pujewf_s6L1p7Js19Om7AfowabOHkzJ5J-rogmLAENN0XUiotw"

URL = "wss://kylin.eos.dfuse.io/v1/stream?token={}".format(KEY)


@asyncio.coroutine
def get():
    websocket = yield from websockets.connect(
        URL, origin="https://ws-my-app.com")

    try:

        data = {
            "type": "get_action_traces",
            "listen": True,
            "req_id": "w454564343",
            "data": {
                "account": "myaccnt",
                "action_name": "attest",
                "with_progress": True
            }
        }

        yield from websocket.send(json.dumps(data))
        while True:
            greeting = yield from websocket.recv()
            print("{}".format(greeting))

    finally:
        yield from websocket.close()


asyncio.get_event_loop().run_until_complete(get())