import datetime

from dfuse.eosio import Eosio


def test_get_block_at_timestamp():
    eosio = Eosio()
    obj = eosio.get_block_at_timestamp(
        time=datetime.datetime.now() - datetime.timedelta(1), comparator="gte"
    )
    print(obj.data)
    assert "block" in obj.data
