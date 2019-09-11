import asyncio
import websockets
import json
from decouple import config

URL = config('WSS_URL')


class DfuseWs:
    """
    This is the base wrapper for interacting with the Dfuse Websocket endpoint.

    The message format is as follows:

        `type`	string	required	The type of the message. See request types below.

        `data`	object	required	A free-form object, specific to the type of request. See request types below.

        `req_id`	string	optional	An ID to associate responses back with the request

        `start_block`	number (integer)	optional	Block at which you want to start processing. 

                        It can be an absolute block number, or a negative value, meaning how many blocks from the current head block on the chain. 

                        Ex: -2500 means 2500 blocks in the past, relative to the head block. 0 means the beginning of the chain.


        `irreversible_only`	boolean	optional, defaults to false	Limits output to events that happened in irreversible blocks. Only supported on `get_action_traces`

        `fetch`	boolean	optional, defaults to false	Whether to fetch an initial snapshot of the requested entity.

        `listen`	boolean	optional, defaults to false	Whether to start listening on changes to the requested entity.

        `with_progress`	number (integer)	optional	Frequency of the progress of blocks processing (within the scope of a req_id). 

    The Request Types are as follows:

        `get_action_traces` - Retrieves a stream of actions, filtered by `receiver` and `account`.

                            - Actions on the EOS blockchain are identified by a triplet `receiver`/`account`/`action_name` * 

                            - The `code` on the `receiver` is called with the method `account`/`action_name` * 

                            - An `action` is considered a “notification” when the `receiver` is different from the `account` field. 

                            - That `receiver` may or may not contain instructions to run for that `account`/`action_name` pair.

        `get_transaction_lifecycle`

        `get_table_rows`

        `get_head_info`

        `unlisten`

        `ping`
    """

    def __init__(self, base_wss_url: str = URL):
        self.wss_url = base_wss_url

    @asyncio.coroutine
    def get(self, token, data: dict, request_id: str, request_type: str = 'get_action_traces', listen: bool = False, irreversible_only: bool = False, fetch: bool = False, with_progress: int = 0, origin: str = 'DFUSE-PY'):

        websocket = yield from websockets.connect(
            f'{self.wss_url}?token={token}', origin=origin)

        try:

            payload = {
                "type": request_type,
                "listen": listen,
                "req_id": request_id,
                "irreversible_only": irreversible_only,
                "data": data
            }

            yield from websocket.send(json.dumps(payload))
            while True:
                response = yield from websocket.recv()
                print(f"{response}")

        finally:
            yield from websocket.close()

    def run(self, token,  data: dict, request_id: str, request_type: str = 'get_action_traces', listen: bool = False, irreversible_only: bool = False, fetch: bool = False, with_progress: int = 5):
        asyncio.get_event_loop().run_until_complete(self.get(token, data, request_id,
                                                             request_type, listen, irreversible_only, fetch, with_progress))


dws = DfuseWs()
