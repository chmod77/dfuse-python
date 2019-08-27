# Defines the Dfuse Object types
import datetime
from typing import List


"""
TableSnapshotResponse
Example table_snapshot response payload:

{"type": "table_snapshot",
 "req_id": "your-request-id",
 "data": {
  "rows": [
   {
    ...
   }]
}}
Name	Type	Options	Description
type	string	required	The table_snapshot string
data	TableRows	required	Rows for the corresponding get_table_rows request. The TableRows object will not contain account nor scope in this case.
The account and scope fields will not be present when the request context makes it obvious what they should be (ex: in the context of a get_table_rows). They will however always be present when querying multi accounts /v0/state/tables/accounts or multi accounts /v0/state/tables/scopes endpoints.


TableDeltaResponse
Example table_delta response payload:

{"type": "table_delta",
 "req_id": "your-request-id",
 "data": {
  "block_num": 123,
  "step": "new",
  "dbop": {
    "op": "ins",
    "old": {},
    "new": {}
  }
}}
Name	Type	Options	Description
type	string	required	The transaction_lifecycle string
data	TableDelta	required	The change operation from a table, navigating forks with the step element.



TableDelta
Example table_delta payload:

{
  "block_num": 123,
  "step": "new",
  "dbop": {
    "op": "upd",
    "old": {},
    "new": {}
  }
}
Name	Type	Options	Description
block_num	number (uint32)	required	Block that produced such a change
step	string	required, one of new, undo, redo	Step in the forks navigation
dbop	DBOp	required	Database operation




StateResponse
Here is a sample response, for a request at block_num: 8:

{
  "up_to_block_id": "0000001000000000000000000000000000000000000000000000000000000000",
  "up_to_block_num": 8,
  "last_irreversible_block_id": "0000000400000000000000000000000000000000000000000000000000000000",
  "last_irreversible_block_num": 4,
  "abi": {
    ...
  },
  "rows": [
    {
      "key": "account123",
      "payer": "account123",
      "json": {
        "owner": "account123"
      },
      "block": 1
    },
    ... or ...
    {
      "key": "account123",
      "payer": "account123",
      "hex": "0011223344556677",
      "block": 2
    },
    ...
  ]
}
Name	Type	Options	Description
up_to_block_id	string	optional	Block ID at which the snapshot was taken when querying the reversible chain segment. This will not be present if querying blocks older than the last irreversible block.
up_to_block_num	number (uint32)	optional	Block number extracted from up_to_block_id if present, provided as a convenience so you don’t need to extract it yourself.
last_irreversible_block_id	string	optional	Last irreversible block considered for this request. The returned snapshot is still for the requested block_num, even though the irreversible block shown here is more recent.
last_irreversible_block_num	number (uint32)	optional	Block number extracted from last_irreversible_block_num, provided as a convenience so you don’t need to extract it yourself.
abi	object	optional	A JSON representation of the ABI that is stored within the account. It is the ABI in effect at the requested block_num.
rows	array<DBRow>	required	An array of rows in the table, sorted by their uint64 key.
The main difference between a StateResponse and a MultiStateResponse is the rows field above.



StateTableRowResponse
Here is a sample response, for a request at block_num: 8:

{
  "up_to_block_id": "0000001000000000000000000000000000000000000000000000000000000000",
  "up_to_block_num": 8,
  "last_irreversible_block_id": "0000000400000000000000000000000000000000000000000000000000000000",
  "last_irreversible_block_num": 4,
  "abi": {
    ...
  },
  "row": {
    "key": "account123",
    "payer": "account123",
    "json": {
      "owner": "account123"
    },
    "block": 1
  }
}
Name | Type | Options | Description —–|——|———|———— up_to_block_id | string | optional | Block ID at which the snapshot was taken when querying the reversible chain segment. This will not be present if querying blocks older than the last irreversible block. up_to_block_num | number (uint32) | optional | Block number extracted from up_to_block_id if present, provided as a convenience so you don’t need to extract it yourself. last_irreversible_block_id | string | optional | Last irreversible block considered for this request. The returned snapshot is still for the requested block_num, even though the irreversible block shown here is more recent. last_irreversible_block_num | number (uint32) | optional | Block number extracted from last_irreversible_block_num, provided as a convenience so you don’t need to extract it yourself. abi | object | optional | A JSON representation of the ABI that is stored within the account. It is the ABI in effect at the requested block_num. row | DBRow | optional | The single row in the table, or null if the primary key does not exist in the table at this block height.

MultiStateResponse
Here is a sample response, for a request at block_num: 8:

{
  "up_to_block_id": "0000001000000000000000000000000000000000000000000000000000000000",
  "up_to_block_num": 8,
  "last_irreversible_block_id": "0000000400000000000000000000000000000000000000000000000000000000",
  "last_irreversible_block_num": 4,
  ...
  "tables": [
    {
      "account": "oo1122334455",
      "scope": "eoscanadacom",
      "rows": [
        {
          "key": "1397706825",
          "payer": "iambillgates",
          "json": {
            "balance": "2000.0000 IPOS"
          }
        }
      ]
    }
  ]
}
Name	Type	Options	Description
up_to_block_id	string	optional	Block ID at which the snapshot was taken when querying the reversible chain segment. This will not be present if querying blocks older than the last irreversible block.
up_to_block_num	number (uint32)	optional	Block number extracted from up_to_block_id if present, provided as a convenience so you don’t need to extract it yourself.
last_irreversible_block_id	string	optional	Last irreversible block considered for this request. The returned snapshot is still for the requested block_num, even though the irreversible block shown here is more recent.
last_irreversible_block_num	number (uint32)	optional	Block number extracted from last_irreversible_block_num, provided as a convenience so you don’t need to extract it yourself.
abi	object	optional	A JSON representation of the ABI that is stored within the account. It is the ABI in effect at the requested block_num.
tables	array<TableRows>	required	An array of tables, one for each queried account, unsorted.



ActionTrace
Example action_trace payload

{
  "type": "action_trace",
  "data": {
    "block_num": 25870889,
    "block_id": "018ac229323f3538cfde5c34f9cfcb1b2d80a4062a822c869d9eb9fcff2235db",
    "block_time": "2018-11-08T13:23:39.5Z",
    "trx_id": "35030b5bfd05f4f5b5bcae68505bf9f2c227a84c6b406dabebe0d8cd0384cd70",
    "idx": 0,
    "depth": 0,
    "trace": {
      "receipt": {
        "receiver": "eosio.msig",
        ...
      },
      "act": {
        "account": "eosio.msig",
        "name": "exec",
        "authorization": [
          {
            "actor": "eoscanadaaaf",
            "permission": "active"
          }
        ],
        "data": {
          "proposer": "eoscanadaaaf",
          "proposal_name": "goincthirthy",
          "executer": "eoscanadaaaf"
        },
        "hex_data": "b08c31c94c833055e05bbeae65341d65b08c31c94c833055"
      },
      "context_free": false,
      "elapsed": 644,
      "console": "",
      "trx_id": "35030b5bfd05f4f5b5bcae68505bf9f2c227a84c6b406dabebe0d8cd0384cd70",
      "block_num": 25870889,
      "block_time": "2018-11-08T13:23:39.500",
      "producer_block_id": "018ac229323f3538cfde5c34f9cfcb1b2d80a4062a822c869d9eb9fcff2235db",
      "account_ram_deltas": [
        {
          "account": "eoscanadaaaf",
          "delta": -323
        }
      ],
      "except": null,
      "inline_traces": []
    },
    "ramops": [
      {
        "op": "deferred_trx_add",
        "action_idx": 0,
        "payer": "eoscanadaaaf",
        "delta": 354,
        "usage": 4027
      },
        ...
    ],
    "dtrxops": [
      {
        "op": "CREATE",
        "action_idx": 0,
        "sender": "eosio.msig",
        "sender_id": "0xe05bbeae65341d65b08c31c94c833055",
        "payer": "eoscanadaaaf",
        "published_at": "2018-11-08T13:23:39.500",
        "delay_until": "2018-11-08T13:23:39.500",
        "expiration_at": "2018-11-08T13:33:39.500",
        "trx_id": "da1abcf7e205cf410c35ba3d474fd8d854a7513d439f7f1188d186493253ed24",
        "trx": {
         ...
        }
      }
    ]
  }
}
Name	Type	Options	Description
block_id	string	required	Block at which we are seeing this action being executed, and for which we are reporting traces.
block_num	number (uint32)	required	Block num corresponding to the block_id
block_time	DateTime	required	Time at which block_id was produced.
trx_id	string	required	ID of transaction that produced these traces
idx	number (uint16)	required	Zero-based index of this action within the transaction. Actions being nestable, this index represents a depth-first search indexing: if action A (index 0) produced an inline action B, then action B is index 1.
depth	number (uint16)	required	Depth of the action relative to the input actions (top-level actions that were defined in the originating transaction, and not inlined as side effects of execution of top-level actions). Actions with depth = 0 are called input actions. Anything above 0 means this is an inline action.
trace	TransactionTrace	required	An execution trace object. This is a standard nodeos trace object. See the reference C++ code here.
ramops	array<RAMOp>	optional	A list of operations on RAM usage, including operation, payer, delta, resulting usage.
dtrxops	array<DTrxOps>	optional	A list of operations on deferred transactions (create, cancel…).



CreationTree
A CreationTree represents the creation-ordered tree of notifications (require_recipient calls), inline actions (send_inline calls) and context free inline actions (send_context_free_inline calls) as defined in the smart contract. The CreationTree is per transaction and might not be present in the returned response. In this case, it means the creation tree is exactly the same as the execution one.

Restrictions The opposite is not true however, it is possible to get a CreationTree and it will still be the same as the execution tree. We trim off the CreationTree as a best effort, it still possible to get a CreationTree mapping 1-to-1 with the execution tree. We suggest computing the tree and checking if there are any differences on the client side if you need to be 100% sure they are different in the presence of the field.

The actual creation order can be different than the execution order, this is because the EOSIO platforms first collect the creation of actions and then execute them, some within a totally new context like send_inline or within the current execution context require_recipient. Moreover, the order in which the execution order is performed is fixed, notifications are executed first (as well as the notifications created as a side-effect of the on-going execution of the notification) then context free inline actions and last the inline actions.

Assuming that you have in your smart contract the following sequence of operations:

send_context_free_inline(...)
require_recipient(...)
send_inline(...)
The creation order is send_context_free_inline, require_recipient, send_inline but the actual execution order and the corresponding execution traces will be in order require_recipient, send_context_free_inline and send_inline instead, quite different!

The CreationTree represents this full ordered hierarchy of actions creation. The tree is encoded as a flat-list each array element being a triplet (encoded in an array): [nodeId, parentId, actionIndex]. Each triplet in the list represents a tree node. The first element of the triplet is a unique id for the node among all nodes in the tree. The second is the parent’s node id, a value of -1 means it’s a root node. The third is the action index within the transaction to map this creation node to, going depth-first in inline_actions, 0-based indexed.

Here an example of creation tree’s flat list, an execution tree and its corresponding creation tree.

CreationTree flat-list received as response from us

[
    [0, -1, 0],
    [1, 0, 1],
    [2, 1, 3],
    [3, 1, 9],
    [4, 0, 2],
    [5, 0, 4],
    [6, 0, 5],
    [7, 0, 7],
    [8, 6, 8],
    [9, 6, 6],
]
Execution traces within the transaction

Execution Tree              (actionIndex 0)
    ├── notify1             (actionIndex 1)
    ├── notify2             (actionIndex 2)
    ├── notify3             (actionIndex 3)
    ├── cf_inline1          (actionIndex 4)
    ├── inline1             (actionIndex 5)
    │   ├── notify4         (actionIndex 6)
    │   ├── cf_inline2      (actionIndex 7)
    │   └── inline3         (actionIndex 8)
    └── inline2             (actionIndex 9)
Represented creation tree, constructed using `CreationTree` flat-list and execution traces

Creation Tree               (0, -1, actionIndex 0)
    ├── notify1             (1, 0, actionIndex 1)
    │   ├── notify3         (2, 1, actionIndex 3)
    │   └── inline2         (3, 1, actionIndex 9)
    ├── notify2             (4, 0, actionIndex 2)
    ├── cf_inline1          (5, 0, actionIndex 4)
    └── inline1             (6, 0, actionIndex 5)
        ├── cf_inline2      (7, 6, actionIndex 7)
        ├── inline3         (8, 6, actionIndex 8)
        └── notify4         (9, 6, actionIndex 6)
Creation Tree Node
Index	Symbolic Name	Type	Description
0	nodeId	int	Unique id for the node among all nodes in the tree.
1	parentId	int	Parent’s node id, a value of -1 means it’s a root node.
2	actionIndex	int	Action index within the transaction to map this creation node to, going depth-first in inline_actions, 0-based indexed.





DBOp
A DBOp represents a database operation. They appear in the table_delta and table_snapshot WS responses. They are also found in the responses from the REST /v0/state/table.

Name	Type	Options	Description
op	string	required	Operation. One of REM (removal), UPD (update) or INS (insertion)
action_idx	number (uint16)	required	Position of the action within the transaction, going depth-first in inline_actions. 0-based index.
account	AccountName	required	Contract account in which this database operation occurred.
scope	Name	not repeated within a Table,
the table specifies the scope	Scope within the contract account, in which the database operation occurred.
key	Name	optional	Represents the primary key of the row in the table.
old	DBRow	optional, depending on op	Contents of the row before a REM or UPD operation.
new	DBRow	optional, depending on op	Contents of the row after an INS or UPD operation.



DBRow
A DBRow represents the contents of a row in a DBOp.

Only one of hex or json will be set. If you requested JSON but ABI-decoding failed, you will receive the encoded binary data in hex alongside an error.

Name	Type	Options	Description
payer	AccountName	required	The account which is billed RAM for the time this row stays in the blockchain state.
hex	hex-encoded byte array	optional	Hex-encoded string representing the binary data of the row
json	Object	optional	Free-form JSON document representing the ABI-decoded row, with the ABI active at the time the operation occurred.
error	string	optional	An error message specifying why the ABI decoding failed, when it did.


RAMOp
A RAM operation is a modification to the RAM consumed by an account. RAM operations on dfuse are scoped down to the action.

Name	Type	Options	Description
op	string	required	Operation. See enum below.
action_idx	number (uint16)	required	Position of the action within the transaction, going depth-first in inline_actions. 0-based index.
payer	AccountName	required	Payer that is credited or debited some RAM usage
delta	number (int64)	required	Number of bytes freed (negative) or consumed (positive) by payer.
usage	number (uint64)	required	Number of bytes available to payer after this operation affects his RAM balance.
Here is a list of operations with the reasons for the consumption:

create_table: creation of a table
deferred_trx_add: storing deferred transaction
deferred_trx_cancel: canceling deferred transaction
deferred_trx_pushed: creating deferred transaction
deferred_trx_removed: executing deferred transaction. NOTE: that this one is the only one that is really scoped to the transaction, and not the action. You can ignore the value of action_idx when op is deferred_trx_removed.
deleteauth: deleting authority
linkauth: linking authority
newaccount: creating new account
primary_index_add: storing row (primary)
primary_index_remove: removing row (primary)
primary_index_update: updating row (primary)
primary_index_update_add_new_payer: storing payer (primary)
primary_index_update_remove_old_payer: removing payer (primary)
remove_table: removing a table
secondary_index_add: storing row (secondary)
secondary_index_remove: removing row (secondary)
secondary_index_update_add_new_payer: storing payer (secondary)
secondary_index_update_remove_old_payer: removing payer (secondary)
setabi: updating ABI for account
setcode: updating contract for account
unlinkauth: unlinking authority
updateauth_create: creating new permission
updateauth_update: updating permission



TableOp
A TableOp represents a table operation, creation or removal of a contract’s table. The table is represents as triplet <account>/<table>/<scope>. No two tables can exist at the same time with the same triplet.

Name	Type	Options	Description
op	string	required	Operation, one of REM (removal) or INS (insertion).
action_idx	number (uint16)	required	Position of the action within the transaction, going depth-first in inline_actions. 0-based index.
account	AccountName	required	Contract account in which this table operation occurred.
table	TableName	required	Contract account’s table affected by this table operation.
scope	Name	required	Table’s scope affected by this table operation.
payer	AccountName	required	Represents the payer of this table, i.e. the table represented by the account/table/scope triplet.



SearchTransactionsResponse
Example payload:

{
  "cursor": "dno3ojdbEpHZV73TfVnvbfWzIpU9BlpvXwo=",
  "transactions": [
    {
      "lifecycle": {
        "transaction_status": "executed",
        "id": "7c5d768973152e0465a2a3eba88689d012ffd4b16cfdd41291e6d7830530d1cb",
        ...
      },
      "action_idx": [
        0
      ]
    }
  ]
}
Name	Type	Options	Description
cursor	string	optional	Cursor to pass back to continue your query. Only present when hitting the limit value. Will be null when reaching the end of the block span searched.
transactions	array<SearchTransactionsRow>	required	List of SearchTransactionsRow objects.
forked_head_warning	boolean	optional	Signals that results previously fetched are at risk of being wrong because of network forks conditions. Will only show when with_reversible was set to true. See pagination for more details.



SearchTransactionsRow
Example payload:

{
  "lifecycle": {
    "transaction_status": "executed",
    "id": "7c5d768973152e0465a2a3eba88689d012ffd4b16cfdd41291e6d7830530d1cb",
    ...
  },
  "action_idx": [
    0
  ]
}
Name	Type	Options	Description
lifecycle	TransactionLifecycle	required	Full transaction where some of its actions matched.
action_idx	array	required	Indexes of the actions (indexed by depth-first search through inline_traces, base 0) that matched the search query.


TransactionLifecycleResponse
Example transaction_lifecycle response payload:

{
  "type": "transaction_lifecycle",
  "data": {
    "lifecycle": {
      "transaction_status":"executed",
      "id": "da1abcf7e205cf410c35ba3d474fd8d854a7513d439f7f1188d186493253ed24",
      "transaction": { ... "actions": [ ... ] ... },
      "execution_trace": { ... },
      ...
    }
  }
}
Here are the fields under data:

Name	Type	Options	Description
type	string	required	The transaction_lifecycle string
data.lifecycle	TransactionLifecycle	required	The lifecycle object being tracked.



TransactionLifecycle
Example TransactionLifecycle payload:

{
  "transaction_status":"executed",
  "id": "da1abcf7e205cf410c35ba3d474fd8d854a7513d439f7f1188d186493253ed24",
  "transaction": { ... "actions": [ ... ] ... },
  "execution_trace": { ... },
  "execution_block_header": { ... },
  "creation_tree": [
    ...
  ],
  "dtrxops": [
    {
      "op": "CREATE",
      ...
      "trx_id": "da1abcf7e205cf410c35ba3d474fd8d854a7513d439f7f1188d186493253ed24",
      "trx": { ... }
    }
  ],
  "ramops": [ ... ],
  "tableops": [ ... ],
  "pub_keys": [
    "EOS86qtjWfMcVJjyLy4TGTybyA8xsFagJtXgwFJC1KR5o7M1ch5ms"
  ],
  "created_by": {
    "src_trx_id": "35030b5bfd05f4f5b5bcae68505bf9f2c227a84c6b406dabebe0d8cd0384cd70",
    "block_num": 25870889,
    "block_id": "018ac229323f3538cfde5c34f9cfcb1b2d80a4062a822c869d9eb9fcff2235db",
    "op": "CREATE",
    "action_idx": 0,
    "sender": "eosio.msig",
    ...
  },
  "canceled_by": null,
  "execution_irreversible": true,
  "creation_irreversible": true,
  "cancelation_irreversible": false
}
Here are the fields under data:

Name	Type	Options	Description
id	string	required	the transaction ID
transaction_status	string	required, one of pending, delayed, canceled, expired, executed, soft_fail, hard_fail	Computed status for the transaction
transaction	Transaction	required	Standard nodeos transaction object
execution_trace	TransactionTrace	optional	Traces of execution. In the case of a deferred transaction, you might not see execution traces
execution_block_header	BlockHeader	optional	Standard block_header object for the block where the transaction got executed
creation_tree	CreationTree	optional	Represents the creation order of actions within this transaction.
dtrxops	array<DTrxOp>	optional	A list of operations on deferred transactions (create, cancel…).
ramops	array<RAMOp>	optional	A list of operations on RAM usage, including operation, payer, delta, resulting usage.
tableops	array<TableOp>	optional	A list of table operations, including operation, contract account, table, scope and payer.
pub_keys	array<string>	optional	List of public keys used to sign the transaction.
created_by	ExtDTrxop	optional	When querying a deferred transaction, reference to the transaction that created it.
canceled_by	ExtDTrxop	optional	Similar to created_by, the reference to another transaction that has canceled this one.
execution_irreversible	boolean	optional	Indicates execution passed irreversibility.
creation_irreversible	boolean	optional	Indicates transaction creation passed irreversibility. Valid only for deferred transactions
cancelation_irreversible	boolean	optional	Indicates cancelation passed irreversibility. Valid only for deferred transactions.
Also see this source code for reference

TransactionTrace
See this source code for reference.

HeadInfo
Example head_info payload:

{
  "type": "head_info",
  "data": {
    "last_irreversible_block_num": 22074884,
    "last_irreversible_block_id": "0150d604868df2ded03bb8e4452cefd0b9c84ae2da31bef6af62b2653c8bb5af",
    "head_block_num": 22075218,
    "head_block_id": "0150d7526b680955eaf4c9d94e17ff3f03d25a1dccb714601173c96b80921362",
    "head_block_time": "2018-11-22T21:00:35.5Z",
    "head_block_producer": "eosswedenorg"
  }
}
Here are the fields under data:

Name	Type	Options	Description
head_block_num	number (uint32)	required	Head block number
head_block_id	string	required	Head block ID
head_block_time	DateTime	required	Head block production time
last_irreversible_block_id	string	required	Block ID of the last irreversible block (at corresponding head block)
last_irreversible_block_num	number (uint32)	required	Block number corresponding to last_irreversible_block_id
"""


class Name:
    """
    An Name is a string that represents a uint64 value, name-encoded using the base32 algorithm. 

    It can only include characters a through z and/or numbers from 1 to 5, and the dot . character. It has a maximum length of 12 or 13 characters (depending on the contents).

    """
    pass


class AccountName(Name):
    """An AccountName is a Name-encoded string that represents an account on the chain."""

    pass


class ActionName(Name):
    """    
    An ActionName is a Name-encoded string that represents a contract’s action.
    """
    pass


class PermissionName(Name):
    """    
    A PermissionName is a Name-encoded string that represents a valid permission on the chain.
    """
    pass


class TableName(Name):
    """
    A TableName is a Name-encoded string that represents a contract’s table on the chain.
    """
    pass


class PublicKey:
    """
    A public key is the publicly known portion of the private key/public key pair that a user can generate.
    """
    pass


class AuthTokenResponse:
    """
        AuthTokenResponse
        Example payload:

        {
        "token": "eyJhbGciOiJ...",
        "expires_at": 1550692172
        }
        Name	Type	Description
        token	string	The JWT to be used with all API calls, including WebSocket.
        expires_at	timestamp	An UNIX timestamp (UTC) indicating when the JWT will expire.
    """

    def __init__(self, token: str, expires_at: datetime.datetime):
        self.token = token
        self.expires_at = expires_at


class DTrxOp:
    ...


class RAMOp:
    ...


class CreationTree:
    ...


class ExtDTrxop:
    ...


class TableOp:
    ...


class TableRows:
    def __init__(self, account, scope, rows):
        self.account = account
        self.scope = scope
        self.rows = rows


class TableSnapshotResponse:
    """
    TableSnapshotResponse
    Example table_snapshot response payload:

    {"type": "table_snapshot",
    "req_id": "your-request-id",
    "data": {
    "rows": [
    {
        ...
    }]
    }}
    Name	Type	Options	Description
    type	string	required	The table_snapshot string
    data	TableRows	required	Rows for the corresponding get_table_rows request. The TableRows object will not contain account nor scope in this case.

    The account and scope fields will not be present when the request context makes it obvious what they should be (ex: in the context of a get_table_rows). 

    They will however always be present when querying multi accounts /v0/state/tables/accounts or multi accounts /v0/state/tables/scopes endpoints.

    """

    def __init__(self, type_: str, data: TableRows):
        self.type = type_
        self.data = TableRows(data)


class BlockHeader:
    ...


class Transaction:
    ...


class TransactionTrace:
    ...


class TransactionLifecycle:
    """
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
    """
    def __init__(self, id: str,
                 transaction_status: str, transaction: Transaction,
                 exectution_trace: TransactionTrace = None, exectution_block_header: BlockHeader = None,
                 creation_tree: CreationTree = None, drtxops: List[DTrxOp] = None,
                 ramops: List[RAMOp] = None, tableops: List[TableOp] = None,
                 pub_keys: List[str] = None, created_by: ExtDTrxop = None, cancelled_by: ExtDTrxop = None, execution_irreversible: bool = None,
                 creation_irreversible: bool = None, cancellation_irreversible: bool = None):
        self.transaction_status = transaction_status
        self.transaction = Transaction(transaction)
        self.exectution_trace = exectution_trace
        self.exectution_block_header = exectution_block_header
        self.creation_tree = creation_tree
        self.drtxops = drtxops
        self.ramops = ramops
        self.tableops = tableops
        self.pub_keys = pub_keys
        self.created_by = created_by
        self.cancelled_by = cancelled_by
        self.execution_irreversible = execution_irreversible
        self.creation_irreversible = creation_irreversible
        self.cancellation_irreversible = cancellation_irreversible
