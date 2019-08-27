from ws import DfuseWs


d = DfuseWs()

payload = {
    "type": "get_action_traces",
    "listen": True,
    "req_id": "your-request-id",
    "irreversible_only": True,
    "data": {
        "accounts": "eosio.token",
        "action_name": "transfer",
                       "with_inline_traces": True,
                       "with_dtrxops": True,
                       "with_ramops": True
    }
}
data = {
    "accounts": "eosio.token",
    "action_name": "transfer",
    "with_inline_traces": True,
    "with_dtrxops": True,
    "with_ramops": True
}

if __name__ == '__main__':
    d.run(data=data, request_id='REQID_DFP', request_type='get_action_traces', listen=True, irreversible_only=False, fetch=True, with_progress=0)
