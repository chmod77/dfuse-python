
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




## Buy me a coffee?

If you feel like buying me a coffee::

```
EOS : greenunicorn
```
