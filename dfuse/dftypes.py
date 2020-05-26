"""
Defines the Dfuse Object types
"""
import datetime
from typing import List


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


class AuthTokenType:
    """
        AuthTokenType
        Example payload:

        {
        "token": "eyJhbGciOiJ...",
        "expires_at": 1550692172
        }
        Name	Type	Description
        token	string	The JWT to be used with all API calls, including WebSocket.
        expires_at	timestamp	An UNIX timestamp (UTC) indicating when the JWT will expire.
    """

    def __init__(self, token: str, expires_at: datetime.datetime, **kwargs):
        self.token = token
        self.expires_at = expires_at


class BlockTimeStampType:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class BlockHeader:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class DTrxOp:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class RAMOp:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class CreationTree:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class ExtDTrxop:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class TableOp:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class DBOp:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class TableRows:
    def __init__(self, account, scope, rows, **kwargs):
        self.account = account
        self.scope = scope
        self.rows = rows


class TableSnapshotType:
    def __init__(self, type_: str, data: TableRows, **kwargs):
        self.type = type_
        self.data = TableRows(**data)


class Transaction:
    def __init__(self, expiration, ref_block_num,
                 ref_block_prefix, max_net_usage_words=0,
                 max_cpu_usage_ms=0, delay_sec=0, context_free_actions=[],
                 actions=[], transaction_extensions=[], signatures=[], context_free_data=[], **kwargs):
        self.expiration = expiration
        self.ref_block_num = ref_block_num
        self.ref_block_prefix = ref_block_prefix
        self.max_net_usage_words = max_net_usage_words
        self.max_cpu_usage_ms = max_cpu_usage_ms
        self.delay_sec = delay_sec
        self.context_free_actions = context_free_actions
        self.actions = actions
        self.transaction_extensions = transaction_extensions
        self.signatures = signatures
        self.context_free_data = context_free_data


class TransactionTrace:
    def __init__(self, id, block_num, block_time, producer_block_id, receipt, elapsed, net_usage, scheduled=False, action_traces=[], failed_dtrx_trace=None, **kwargs):
        self.id = id
        self.block_num = block_num
        self.block_time = block_time
        self.producer_block_id = producer_block_id
        self.receipt = receipt
        self.elapsed = elapsed
        self.net_usage = net_usage
        self.scheduled = scheduled
        self.action_traces = action_traces
        self.failed_dtrx_trace = failed_dtrx_trace
        self.except_ = kwargs.get('except')


class TransactionLifecycle:
    def __init__(self, id: str,
                 transaction_status: str, transaction: Transaction,
                 execution_trace: TransactionTrace, execution_block_header: BlockHeader = None,
                 creation_tree: CreationTree = None, dtrxops: List[DTrxOp] = None, dbops: List[DBOp] = None,
                 ramops: List[RAMOp] = None, tableops: List[TableOp] = None,
                 pub_keys: List[str] = None, created_by: ExtDTrxop = None, canceled_by: ExtDTrxop = None,
                 execution_irreversible: bool = None,
                 creation_irreversible: bool = None, cancelation_irreversible: bool = None, **kwargs):
        self.id = id
        self.transaction_status = transaction_status
        self.transaction = Transaction(**transaction)
        self.execution_trace = TransactionTrace(**execution_trace)
        self.execution_block_header = execution_block_header
        self.creation_tree = creation_tree
        self.dtrxops = dtrxops
        self.ramops = ramops
        self.tableops = tableops
        self.pub_keys = pub_keys
        self.created_by = created_by
        self.canceled_by = canceled_by
        self.execution_irreversible = execution_irreversible
        self.creation_irreversible = creation_irreversible
        self.cancelation_irreversible = cancelation_irreversible
        self.data=self.__dict__


class ABIType:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.block_num = kwargs.get('block_num')
        self.account = kwargs.get('account')
        self.abi = kwargs.get('abi')


class Bin2JSONType:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.block_num = kwargs.get('block_num')
        self.account = kwargs.get('account')
        self.table = kwargs.get('table')
        self.rows = kwargs.get('rows')


class KeyAccountsType:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.block_num = kwargs.get('block_num')
        self.account_names = kwargs.get('account_names')


class PermissionLinkType:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.up_to_block_id = kwargs.get('up_to_block_id')
        self.up_to_block_num = kwargs.get('up_to_block_num')
        self.last_irreversible_block_id = kwargs.get(
            'last_irreversible_block_id')
        self.last_irreversible_block_num = kwargs.get(
            'last_irreversible_block_num')
        self.linked_permissions = kwargs.get('linked_permissions')


class StateType:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.up_to_block_id = kwargs.get('up_to_block_id')
        self.up_to_block_num = kwargs.get('up_to_block_num	')
        self.last_irreversible_block_id = kwargs.get(
            'last_irreversible_block_id')
        self.last_irreversible_block_num = kwargs.get(
            'last_irreversible_block_num')
        self.abi = kwargs.get('abi')
        self.rows = kwargs.get('rows')


class StateTableRowType:
    def __init__(self, *args, **kwargs):
        self.data = kwargs
        self.last_irreversible_block_id = kwargs.get(
            'last_irreversible_block_id')
        self.last_irreversible_block_num = kwargs.get(
            'last_irreversible_block_num')
        self.row = kwargs.get('row')


class TableScopeType:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.block_num = kwargs.get('block_num')
        self.scopes = kwargs.get('scopes')


class MultiStateType:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.up_to_block_id = kwargs.get('up_to_block_id')
        self.up_to_block_num = kwargs.get('up_to_block_num')
        self.last_irreversible_block_id = kwargs.get(
            'last_irreversible_block_id')
        self.last_irreversible_block_num = kwargs.get(
            'last_irreversible_block_num')
        self.abi = kwargs.get('abi')
        self.tables = kwargs.get('tables')


class DfuseError:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.code = kwargs.get('code')
        self.trace_id = kwargs.get('trace_id')
        self.message = kwargs.get('message')
