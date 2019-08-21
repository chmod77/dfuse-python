
**dfuse** is an open source library written in Python providing an easy to use wrapper around the [dfuse.io](https://dfuse.io/) API. This library has been tested with Python 3.6.x and Python 3.7.x.


## Installation:
### - TODO
## API Documentation:


This API can currently retrieve the following data from [dfuse.io](https://dfuse.io/):

#### **`GET /v0/block_id/by_time/by_time?time=2019-03-04T10:36:14.5Z&comparator=gte`**
- **`Description`** - Fetches the block ID, time and block number for the given timestamp, using the ```time``` and ```comparator```  parameters.
- **`Types`** - ```time``` - datetime
              - ```comparator``` - string
- **`Optional parameters:`**
    - None

```python
>>> from dfuse import Dfuse
>>> dfuse_ = Dfuse()
>>> import datetime
>>> dfuse_.get_block_at_timestamp(time=datetime.datetime.now()-datetime.timedelta(1), comparator='gte')

{'block': 
    {
        'id': '04763b536d8da0a1d7e10e666333b51efec16d5c5264a69f736acf37a14dec2b', 
        'num': 74857299, 
        'time': '2019-08-19T14:32:59Z'
    }
}

```

#### **`GET /v0/transactions/:id`**
- **`Description`** - Fetches the transaction lifecycle associated with the provided path parameter ```:id```.

- **`Types`** - ```id``` - string
            
- **`Optional parameters:`**
    - None

```python
>>> from dfuse import Dfuse
>>> dfuse_ = Dfuse()
>>> dfuse_.get_transaction_lifecycle(id='1d5f57e9392d045ef4d1d19e6976803f06741e11089855b94efcdb42a1a41253')

{
    'transaction_status': 'executed',
    'id': '1d5f57e9392d045ef4d1d19e6976803f06741e11089855b94efcdb42a1a41253',
    'transaction': {'expiration': '2019-04-16T14:36:11',
    'ref_block_num': 65222,
    'ref_block_prefix': 943310534,
    'max_net_usage_words': 0,
    'max_cpu_usage_ms': 0,
    'delay_sec': 0,
    'context_free_actions': [],
    'actions': [{'account': 'maouehmaoueh',
        'name': 'cfainline',
        'authorization': [{'actor': 'maouehmaoueh', 'permission': 'active'}],
        'hex_data': '03313233'}],
    'transaction_extensions': [],
    'signatures': ['SIG_K1_Jyv32XzrAGQepnk7p3YwXbRyNcp6Cztt8peR41GjfJ5hjDhjNfyf4ViubcShaDGd1BB9NEKGRrGjsQadzvwKrp7Wkjx9kh'],
    'context_free_data': []},
    'execution_trace': {'id': '1d5f57e9392d045ef4d1d19e6976803f06741e11089855b94efcdb42a1a41253',
    'block_num': 53280461,
    'block_time': '2019-04-16T14:35:41.5',
    'producer_block_id': '032cfecd63f2e42da2fb5b7f632acadbe5153756db615c5d28bbc99f9bd0976d',
    'receipt': {'status': 'executed',
    'cpu_usage_us': 1191,
    'net_usage_words': 12},
    'elapsed': 71934,
    'net_usage': 96,
    'scheduled': False,
    'action_traces': [{'receipt': {'receiver': 'maouehmaoueh',
        'act_digest': '5a2ffd1d0376049b5fcaa7d5f122723973c8fea40de9aba059bc439b4f77fd5e',
        'global_sequence': '6249291689',
        'auth_sequence': [['maouehmaoueh', 13]],
        'recv_sequence': 5,
        'code_sequence': 2,
        'abi_sequence': 1},
        'act': {'account': 'maouehmaoueh',
        'name': 'cfainline',
        'authorization': [{'actor': 'maouehmaoueh', 'permission': 'active'}],
        'data': {'data': '123'},
        'hex_data': '03313233'},
        'context_free': False,
        'elapsed': 71857,
        'console': '',
        'trx_id': '1d5f57e9392d045ef4d1d19e6976803f06741e11089855b94efcdb42a1a41253',
        'block_num': 53280461,
        'block_time': '2019-04-16T14:35:41.5',
        'producer_block_id': '032cfecd63f2e42da2fb5b7f632acadbe5153756db615c5d28bbc99f9bd0976d',
        'account_ram_deltas': None,
        'except': None,
        'inline_traces': [{'receipt': {'receiver': 'dfuseiohooks',
        'act_digest': '469d68d4e68c0adc6fd302ca60b4d27256400965b90baf7a5736c9e0ed0b3d0f',
        'global_sequence': '6249291690',
        'auth_sequence': [],
        'recv_sequence': 2,
        'code_sequence': 0,
        'abi_sequence': 1},
        'act': {'account': 'dfuseiohooks',
        'name': 'event',
        'data': {'data': 'testing=123', 'key': ''},
        'hex_data': '000b74657374696e673d313233'},
        'context_free': True,
        'elapsed': 11,
        'console': '',
        'trx_id': '1d5f57e9392d045ef4d1d19e6976803f06741e11089855b94efcdb42a1a41253',
        'block_num': 53280461,
        'block_time': '2019-04-16T14:35:41.5',
        'producer_block_id': '032cfecd63f2e42da2fb5b7f632acadbe5153756db615c5d28bbc99f9bd0976d',
        'account_ram_deltas': None,
        'except': None,
        'inline_traces': None}]}],
    'failed_dtrx_trace': None,
    'except': None},
    'execution_block_header': {'timestamp': '2019-04-16T14:35:41.5',
    'producer': 'bitfinexeos1',
    'confirmed': 0,
    'previous': '032cfeccf3b57dd793d3ff831adb381225fa7c2b4a998a3c16502c2774581e36',
    'transaction_mroot': 'a4317c9ce3c3925fac8bda2463a06d5b5876b37ea4b0b2af36bb42d028910a66',
    'action_mroot': '16187708fc3827f31d2fbe8ecf6c1877e2b5f0050e63f025edd01eeff4dec82f',
    'schedule_version': 773,
    'new_producers': None,
    'header_extensions': []},
    'dtrxops': None,
    'creation_tree': [],
    'dbops': None,
    'ramops': None,
    'tableops': None,
    'pub_keys': ['EOS8b3K9r6mLDykeL7GzGJCFt9Z5SRSHSXFT77yHz8e3z7en1tFwG'],
    'created_by': None,
    'canceled_by': None,
    'execution_irreversible': True,
    'creation_irreversible': True,
    'cancelation_irreversible': False
 }
```
#### **`GET /v0/state/abi?account={account}&json={true/false}&block_num=int`**
- **`Description`** - Fetch the ABI for a given contract ```account```, at any ```block_num``` height.
                    The ```block_num``` parameter determines for which block you want the given ABI. This can be anywhere in the chain’s history. 
                    
    If the requested ```block_num``` is irreversible, you will get an immutable ABI. If the ABI has changed while still in a reversible chain, you will get this new ABI, but it is not guaranteed to be the view that will pass irreversibility. Inspect the returned block_num parameter of the response to understand from which longest chain the returned ABI is from.

    The returned ABI is the one that was active at the block_num requested

- **`Types`** 
    - ```account``` - string (required)
    - ```json```    - bool (optional, defaults to False)
    - ```block_num``` - int (Optional - defaults to ```head block num```)
            
- **`Optional parameters:`**
    - ```json```
    - ```block_num```


```python
>>> from dfuse import Dfuse
>>> dfuse_ = Dfuse()
>>> dfuse_.fetch_abi(account='arbarotokenn', block_num=57202657)

{'block_num': 57202658,
 'account': 'arbarotokenn',
 'abi': '0e656f73696f3a3a6162692f312e310009076163636f756e7400020762616c616e6365056173736574096c617374636c61696d05617373657405636c61696d0002056f776e6572046e616d6508746f6b656e73796d0673796d626f6c05636c6f73650002056f776e6572046e616d650673796d626f6c0673796d626f6c06637265617465000206697373756572046e616d650e6d6178696d756d5f737570706c790561737365740e63757272656e63795f7374617473000406737570706c790561737365740a6d61785f737570706c7905617373657406697373756572046e616d650e746f74616c6469766964656e6473056173736574056973737565000302746f046e616d65087175616e74697479056173736574046d656d6f06737472696e67046f70656e0003056f776e6572046e616d650673796d626f6c0673796d626f6c0972616d5f7061796572046e616d65067265746972650002087175616e74697479056173736574046d656d6f06737472696e67087472616e7366657200040466726f6d046e616d6502746f046e616d65087175616e74697479056173736574046d656d6f06737472696e67070000000000e94c4405636c61696d00000000000085694405636c6f73650000000000a86cd44506637265617465000000000000a531760569737375650000000000003055a5046f70656e0000000000a8ebb2ba0672657469726500000000572d3ccdcd087472616e736665720002000000384f4d1132036936340000076163636f756e740000000000904dc60369363400000e63757272656e63795f737461747300000000'
}

```

# TODO:

-  **POST** ```/v0/state/abi/bin_to_json```: Decode binary rows (in hexadecimal string) for a given table against the ABI of a given contract account, at any block height.

-  **GET** ```/v0/state/permission_links```: Fetching snapshots of any account’s linked authorizations on the blockchain, at any block height.

-  **GET** ```/v0/state/table```: Fetching snapshots of any table on the blockchain, at any block height.

-  **GET** ```/v0/state/table/accounts```: Fetching snapshots of any table on the blockchain, at any block height, for a list of accounts (contracts).

-  **GET** ```/v0/state/table/scopes```: Fetching snapshots of any table on the blockchain, at any block height, for a list of scopes for a given account (contract).

-  **GET** ```/v0/search/transactions```: Structure Query Engine (SQE), for searching the whole blockchain history and get fast and precise results.

-  **POST** ```/v1/chain/push_transaction```: Drop-in replacement for submitting a transaction to the network, but can optionally block the request until the transaction is either in a block or in an irreversible block.

- Other ```/v1/chain/```: Reverse-proxy of all standard chain requests to a well-connected node.

- **WEBSOCKETS**

- **GRAPHQL**



## Buy me a coffee?

If you feel like buying me a coffee::

```
EOS : greenunicorn
```
