
**dfuse** is an open source library written in Python providing an easy to use wrapper around the [dfuse.io](https://dfuse.io/) API. This library has been tested with Python 3.6.x and Python 3.7.x.


## Installation:

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
>>> import datetime
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


## Buy me a coffee?

If you feel like buying me a coffee::

```
EOS : greenunicorn
```
