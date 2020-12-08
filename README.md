
**dfuse** is an open source library written in Python providing an easy to use wrapper around the [dfuse.io](https://dfuse.io/) API. This library has been tested with Python 3.6.x, 3.7.x 3.8.x.

## Installation
From source use:

    $ python setup.py install

or install from PyPi:

```bash
$ pipenv install dfuse
```
    
- It is important that you do this from a virtual environment.


## Prerequisites

   To get up and rolling, create a .env or .ini file in the project folder, with contents copied from the `example.env` file. (as required by [python decouple](https://pypi.org/project/python-decouple/))

   Make sure to substitute the predefined keys with the appropriate ones.

   ```API_KEY = YOUR_API_KEY_HERE```

   ```EOS_BASE_URL = https://eos.dfuse.eosnation.io OR any of the REST Endpoints below``` 

   ```EOS_BLOCK_TIME_URL = /v0/block_id/by_time```

   ```EOS_TRX_URL = /v0/transactions```

   ```EOS_STATE_BASE_URL = /v0/state```

**ENSURE NO trailing slash at the end of the *BASE_URL**

 Supported list of EOSIO Networks (Endpoints):

 1. **EOS Mainnet**
    
    Chain ID: `aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906`

    REST Endpoint: https://eos.dfuse.eosnation.io/

    Websocket: wss://eos.dfuse.eosnation.io/v1/stream

 2. **EOSIO Testnet**

    Chain ID: `0db13ab9b321c37c0ba8481cb4681c2788b622c3abfd1f12f0e5353d44ba6e72`

    REST: https://testnet.eos.dfuse.io/

    Websocket: wss://testnet.eos.dfuse.io/v1/stream

    GraphQL: https://testnet.eos.dfuse.io/graphql

 3. **CryptoKylin**

    Chain ID: `5fff1dae8dc8e2fc4d5b23b2c7665c97f9e9d8edf2b6485a86ba311c25639191`

    REST	https://kylin.eos.dfuse.io/

    WebSocket	wss://kylin.eos.dfuse.io/v1/stream

    GraphQL	https://kylin.eos.dfuse.io/graphql 

 4. **WAX Mainnet**

    Chain ID: `1064487b3cd1a897ce03ae5b6a865651747e2e152090f99c1d19d44e01aea5a4`

    REST	https://mainnet.wax.dfuse.io/

    WebSocket	wss://mainnet.wax.dfuse.io/v1/stream

    GraphQL	https://mainnet.wax.dfuse.io/graphql


Use the `REST` endpoint values as your `EOS_BASE_URL`

   You can also define these values as environment variables.

If the dfuse API is upgraded to another version, say v1, it is easier to switch to that with minimal changes. You only edit your .env file to match the changes.

## JWT Caching

Short-time lived JWT Tokens are persisted on a local sqlite3 database, and are usable for upto 22 hours.

## API Documentation:


This API can currently retrieve the following data from [dfuse.io](https://dfuse.io/):

#### **`GET /v0/block_id/by_time/by_time?time=2019-03-04T10:36:14.5Z&comparator=gte`**
- **`Description`** - Fetches the block ID, time and block number for the given timestamp, using the ```time``` and ```comparator```  parameters.
- **`Types`** 

    - ```time``` - datetime
    - ```comparator``` - string
- **`Optional parameters:`**
    - None
- This returns a `BlockTimeStampType`

- You can access all the fields in the response by getting the `data` key, as shown in the following example.
```python
>>> from dfuse import Eosio
>>> eosio = Eosio()
>>> import datetime
>>> obj = eosio.get_block_at_timestamp(time=datetime.datetime.now()-datetime.timedelta(1), comparator='gte')
>>> obj

<dfuse.eosio.types.BlockTimeStampType at 0x7fcfc746abb0>

>>> obj.data

{
    'block': 
        {
            'id': '095227fa85998bfefb6c474be42d8d6f1e890f152c7047570b8ababa73c12783',
            'num': 156379130,
            'time': '2020-12-07T10:37:15.5Z'
        }
}

```

#### **`GET /v0/transactions/:id`**
- **`Description`**  
    
    Fetches the transaction lifecycle associated with the provided path parameter ```:id```.

- **`Types`** 
    
    - ```id``` - string
            
- **`Optional parameters:`**
    - None

```python
>>> from dfuse import Eosio
>>> eosio = Eosio()
>>> obj = eosio.get_transaction_lifecycle(id='1d5f57e9392d045ef4d1d19e6976803f06741e11089855b94efcdb42a1a41253')

>>> obj

   <dfuse.eosio.types.TransactionLifecycle at 0x7fcfc747c3d0>


>>> obj.data

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
        'actions': [{
            'account': 'maouehmaoueh',
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

 >>> obj.transaction_status

    'executed'
```

#### **`GET /v0/state/abi?account={account}&json={true/false}&block_num=int`**
- **`Description`**  
    
    Fetch the ABI for a given contract ```account```, at any ```block_num``` height.
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
>>> obj = dfuse_.fetch_abi(account='arbarotokenn', block_num=57202657)

>>> obj

    <dfuse.dftypes.ABIType at 0x7f54dc041828>

>>> obj.data

    {'block_num': 57202658,
    'account': 'arbarotokenn',
    'abi': {'version': 'eosio::abi/1.1',
    'structs': [{'name': 'account',
        'base': '',
        'fields': [{'name': 'balance', 'type': 'asset'},
        {'name': 'lastclaim', 'type': 'asset'}]},
    {'name': 'claim',
        'base': '',
        'fields': [{'name': 'owner', 'type': 'name'},
        {'name': 'tokensym', 'type': 'symbol'}]},
    {'name': 'close',
        'base': '',
        'fields': [{'name': 'owner', 'type': 'name'},
        {'name': 'symbol', 'type': 'symbol'}]},
    {'name': 'create',
        'base': '',
        'fields': [{'name': 'issuer', 'type': 'name'},
        {'name': 'maximum_supply', 'type': 'asset'}]},
    {'name': 'currency_stats',
        'base': '',
        'fields': [{'name': 'supply', 'type': 'asset'},
        {'name': 'max_supply', 'type': 'asset'},
        {'name': 'issuer', 'type': 'name'},
        {'name': 'totaldividends', 'type': 'asset'}]},
    {'name': 'issue',
        'base': '',
        'fields': [{'name': 'to', 'type': 'name'},
        {'name': 'quantity', 'type': 'asset'},
        {'name': 'memo', 'type': 'string'}]},
    {'name': 'open',
        'base': '',
        'fields': [{'name': 'owner', 'type': 'name'},
        {'name': 'symbol', 'type': 'symbol'},
        {'name': 'ram_payer', 'type': 'name'}]},
    {'name': 'retire',
        'base': '',
        'fields': [{'name': 'quantity', 'type': 'asset'},
        {'name': 'memo', 'type': 'string'}]},
    {'name': 'transfer',
        'base': '',
        'fields': [{'name': 'from', 'type': 'name'},
        {'name': 'to', 'type': 'name'},
        {'name': 'quantity', 'type': 'asset'},
        {'name': 'memo', 'type': 'string'}]}],
    'actions': [{'name': 'claim', 'type': 'claim', 'ricardian_contract': ''},
    {'name': 'close', 'type': 'close', 'ricardian_contract': ''},
    {'name': 'create', 'type': 'create', 'ricardian_contract': ''},
    {'name': 'issue', 'type': 'issue', 'ricardian_contract': ''},
    {'name': 'open', 'type': 'open', 'ricardian_contract': ''},
    {'name': 'retire', 'type': 'retire', 'ricardian_contract': ''},
    {'name': 'transfer', 'type': 'transfer', 'ricardian_contract': ''}],
    'tables': [{'name': 'accounts', 'index_type': 'i64', 'type': 'account'},
    {'name': 'stat', 'index_type': 'i64', 'type': 'currency_stats'}]}}


```

#### **`POST /v0/state/abi/bin_to_json`**
- **`Description`**  
    
    Decodes binary rows (in hexadecimal string) for a given table against the ABI of a given contract account, at any block height.
                
    The returned ABI is the one that was active at the block_num requested.

    The block_num parameter determines for which block you want to decode rows against. This can be anywhere in the chain’s history.

    If the requested `block_num` is irreversible, decoding will be performed against an immutable ABI. If the ABI has changed while still in a reversible chain, decoding will be performed against this new ABI, but it is not guaranteed to be the view that will pass irreversibility. Inspect the returned `block_num` parameter of the response to understand from which longest chain the returned ABI is from.

- **`Types`** 
    - ```account``` - string (required)
    - ```table``` - The name-encoded table name you want to retrieve (contract dependent)
    - ```hex_rows``` - An array of hexadecimal rows to decode. Each row must be a valid hexadecimal string representation of the row to decode against the ABI.
    - ```block_num``` - int (Optional - defaults to ```head block num```)
            
- **`Optional parameters:`**
    - ```block_num```

```python
>>> from dfuse import Dfuse
>>> dfuse_ = Dfuse()
>>> obj = dfuse_.bin_to_json(account='eosio.token', table='accounts',  hex_rows=["aa2c0b010000000004454f5300000000"], block_num=2600000)

>>> obj

    <dfuse.dftypes.Bin2JSONType at 0x7f54c4763908>

>>> obj.data

    {
        'block_num': 181,
        'account': 'eosio.token',
        'table': 'accounts',
        'rows': [
            {
                'balance': '1750.9546 EOS'
            }
        ]
    }

>>> obj.account

    'eosio.token'

>>> obj.block_num

    181

```

#### **`GET /v0/state/key_accounts`**
- **`Description`** 
    
    Fetches the accounts controlled by the given public key, at any block height.

    NOTE: this endpoint is a drop-in replacement for the /v1/history/get_key_accounts API endpoint from standard nodeos. Simply tweak the URL, and add the Bearer token.

    The block_num parameter determines for which block height you want a list of accounts associated to the given public key. This can be anywhere in the chain’s history.

    If the requested block_num is irreversible, you will get an immutable list of accounts. Otherwise, there are chances that the returned value moves as the chain reorganizes.
                    

- **`Types`** 
    - ```public_key``` - The public key to fetch controlled accounts for. string (required)

    - ```block_num``` - int (Optional - defaults to ```head block num```)
            
- **`Optional parameters:`**
    - ```block_num```

```python

>>> from dfuse import Dfuse
>>> dfuse_ = Dfuse()
>>> obj = dfuse_.get_key_accounts(public_key='EOS744heXNxjLamUjLxaLpn6gREh3CVf5VvFESq9sG969VmcNYyq6')

>>> obj

    <dfuse.dftypes.KeyAccountsType at 0x7f54c7169be0>

>>> obj.data

    {'block_num': 76752386, 'account_names': ['greenunicorn']}

>>> obj.block_num

    76752386

>>> obj.account_names

    ['greenunicorn']
```


#### **`GET /v0/state/permission_links`**
- **`Description`** 
    
    Fetches snapshots of any account’s linked authorizations on the blockchain, at any block height.

    The block_num parameter determines for which block you want a linked authorizations snapshot. This can be anywhere in the chain’s history.

    If the requested block_num is irreversible, you will get an immutable snapshot. If the block_num is still in a reversible chain, you will get a full consistent snapshot, but it is not guaranteed to be the view that will pass irreversibility. Inspect the returned up_to_block_id parameter to understand from which longest chain the returned value is a snapshot of.
                    

- **`Types`** 
    - ```account``` - string (required)

    - ```block_num``` - int (Optional - defaults to ```head block num```)
            
- **`Optional parameters:`**
    - ```block_num```


```python
>>> from dfuse import Dfuse
>>> dfuse_ = Dfuse()
>>> obj = dfuse_.get_permission_links(account='eoscanadacom', block_num=25000000)  

>>> obj

   <dfuse.dftypes.PermissionLinkType at 0x7f54c7501c50>

>>> obj.data

    {'last_irreversible_block_id': '04931d68265c1fba52f772e031e67d2f16d898ed0ee0c60384db163345e7d0f1',
    'last_irreversible_block_num': 76750184,
    'linked_permissions': [{'contract': 'eosforumdapp',
    'action': 'post',
    'permission_name': 'day2day'},
    {'contract': 'eosforumdapp',
    'action': 'status',
    'permission_name': 'day2day'},
    {'contract': 'eosforumdapp',
    'action': 'unpost',
    'permission_name': 'day2day'},
    {'contract': 'eosio',
    'action': 'claimrewards',
    'permission_name': 'claimer'},
    {'contract': 'eosio', 'action': 'regproducer', 'permission_name': 'day2day'},
    {'contract': 'eosio', 'action': 'unregprod', 'permission_name': 'day2day'},
    {'contract': 'theblacklist',
    'action': 'sethash',
    'permission_name': 'blacklistops'}]}

>>> obj.last_irreversible_block_id

    '04931d68265c1fba52f772e031e67d2f16d898ed0ee0c60384db163345e7d0f1'

>>> obj.last_irreversible_block_num 
    
    76750184

```

#### **`GET/v0/state/table`**
- **`Description`** 
    
    Fetches the state of any table, at any block height.

    The block_num parameter determines for which block you want a table snapshot. This can be anywhere in the chain’s history.

    If the requested block_num is irreversible, you will get an immutable snapshot. If the block_num is still in a reversible chain, you will get a full consistent snapshot, but it is not guaranteed to pass irreversibility. Inspect the returned up_to_block_id parameter to understand from which longest chain the returned value is a snapshot of.
                    

- **`Types`** 

    - ```account``` - string (required)

    - ```scope``` - The name-encoded scope of the table you are requesting. (required)

    - ```table``` - table name you want to retrieve (required)

    - ```block_num``` - int (Optional - defaults to ```head block num```)

    - ```json```  - boolean (optional, defaults to false)

    - ```key_type``` - How to represent the row keys in the returned table. string (optional, defaults to `name`) 

    - Valid `key_type`s:
                    
        - `name` (default) for EOS name-encoded base32 representation of the row key
        - `hex` for hexadecimal encoding, ex: abcdef1234567890
        - `hex_be` for big endian hexadecimal encoding, ex: 9078563412efcdab
        - `uint64` for string encoded uint64
            
- **`Optional parameters:`**
    - ```block_num```
    - ```json```
    - ```key_type```

```python

>>> from dfuse import Dfuse
>>> dfuse_ = Dfuse()
>>> obj = dfuse_.get_table(account='eosio.token', scope='greenunicorn', table='accounts', block_num=74000000) 

>>> obj

    <dfuse.dftypes.StateType at 0x7f54c711f908>

>>> obj.data

    {'last_irreversible_block_id': '04932bcb8edd41317814654da379057d6a2f880aaf2e095a602b997eedc5c143',
        'last_irreversible_block_num': 76753867,
        'rows': [{'key': '........ehbo5',
        'payer': 'greenunicorn',
        'json': {'balance': '0.7585 EOS'}}
        ]
    }

>>> obj.obj.last_irreversible_block_id

    '04932bcb8edd41317814654da379057d6a2f880aaf2e095a602b997eedc5c143'

```

#### **`GET /v0/state/tables/accounts`**
- **`Description`** 
    
    Fetches the state of any table, at any block height.

    The block_num parameter determines for which block you want a table snapshot. This can be anywhere in the chain’s history.

    If the requested block_num is irreversible, you will get an immutable snapshot. If the block_num is still in a reversible chain, you will get a full consistent snapshot, but it is not guaranteed to pass irreversibility. Inspect the returned up_to_block_id parameter to understand from which longest chain the returned value is a snapshot of.
                    

- **`Types`** 
 - ```account``` - string (required), separated by |

    - ```scope``` - The name-encoded scope of the table you are requesting. (required)

    - ```table``` - table name you want to retrieve (required)

    - ```block_num``` - int (Optional - defaults to ```head block num```)

    - ```json```  - boolean (optional, defaults to false)

    
```python

>>> from dfuse import Dfuse

>>> df = Dfuse()

>>> obj = df.get_table_accounts(accounts="eosadddddddd|tokenbyeocat|ethsidechain|epraofficial|alibabapoole|hirevibeshvt|oo1122334455|irespotokens|publytoken11|parslseed123|trybenetwork|zkstokensr4u", scope="b1", table="accounts", block_num=45000000, json="true")

>>> obj

    <dfuse.dftypes.MultiStateType at 0x7fe61111d820>

>>> obj.data

      {'last_irreversible_block_id': '',
        'last_irreversible_block_num': 0,
        'tables': [{'account': 'tokenbyeocat', 'scope': 'b1', 'rows': []},
        {'account': 'irespotokens', 'scope': 'b1', 'rows': []},
        {'account': 'parslseed123', 'scope': 'b1', 'rows': []},
        {'account': 'trybenetwork', 'scope': 'b1', 'rows': []},
        {'account': 'ethsidechain',
        'scope': 'b1',
        'rows': [{'key': '......2cel2o5',
            'payer': 'eos1kissgirl',
            'json': {'balance': '2000.0001 EETH'}}]},
        {'account': 'oo1122334455',
        'scope': 'b1',
   'rows': [{'key': '......2ndxc4d',
     'payer': 'guztemzzgyge',
     'json': {'balance': '4550.0000 IPOS'}}]},
     'tables': [{'account': 'tokenbyeocat', 'scope': 'b1', 'rows': []},
        {'account': 'irespotokens', 'scope': 'b1', 'rows': []},
        {'account': 'parslseed123', 'scope': 'b1', 'rows': []},
        {'account': 'trybenetwork', 'scope': 'b1', 'rows': []},
        {'account': 'ethsidechain',
        'scope': 'b1',
        'rows': [{'key': '......2cel2o5',
            'payer': 'eos1kissgirl',
            'json': {'balance': '2000.0001 EETH'}}]},
        {'account': 'oo1122334455',
        'scope': 'b1',
        'rows': [{'key': '......2ndxc4d',
            'payer': 'guztemzzgyge',
            'json': {'balance': '4550.0000 IPOS'}}]},
```



**GET** ```/v0/state/tables/scopes```: Fetching snapshots of any table on the blockchain, at any block height, for a list of scopes for a given account (contract).

- **`Description`** 
    
    Fetches all rows for a table in a given contract for a group of scopes, at any block heigh

    Most parameters are similar to the /v0/state/table request, except for the scopes parameter, which accepts a list of name-encoded scopes separated by the pipe character (|).

    The output format is slightly different too.
                    

- **`Types`** 

    - ```account``` - string (required)

    - ```scope``` - The name-encoded scope of the table you are requesting. (required)

    - ```table``` - table name you want to retrieve (required)

    - ```block_num``` - int (Optional - defaults to ```head block num```)

    - ```json```  - boolean (optional, defaults to false)

    - ```key_type``` - How to represent the row keys in the returned table. string (optional, defaults to `name`) 

    - Valid `key_type`s:
                    
        - `name` (default) for EOS name-encoded base32 representation of the row key
        - `hex` for hexadecimal encoding, ex: abcdef1234567890
        - `hex_be` for big endian hexadecimal encoding, ex: 9078563412efcdab
        - `uint64` for string encoded uint64

    - ```with_block_num``` - Optional, Boolean. Defaults to false | Will return one `block_num` with each row. Represents the block at which that row was last changed.

    - ```with_abi``` - Boolean     Defaults to false | Return the ABI in effect at block `block_num`.

            
- **`Optional parameters:`**
    - ```block_num```
    - ```json```
    - ```key_type```
    - ```with_block_num```
    - ```with_abi```




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
