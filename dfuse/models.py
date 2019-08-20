# Defines the Dfuse Object types
import datetime
from typing import List


class AuthTokenResponse:
    def __init__(self, token: str, expires_at: datetime.datetime):
        self.token = token
        self.expires_at = expires_at


class TableRows:
    def __init__(self, account, scope, rows):
        self.account = account
        self.scope = scope
        self.rows = rows


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


class TableSnapshotResponse:
    def __init__(self, type_: str, data: TableRows):
        self.type = type_
        self.data = data


class BlockHeader:
    ...


class Transaction:
    ...


class TransactionTrace:
    ...


class TransactionLifecycle:
    def __init__(self, id: str,
                 transaction_status: str, transaction: Transaction,
                 exectution_trace: TransactionTrace = None, exectution_block_header: BlockHeader = None,
                 creation_tree: CreationTree=None, drtxops: List[DTrxOp]=None,
                 ramops: List[RAMOp]=None, tableops: List[TableOp]=None,
                 pub_keys: List[str]=None, created_by: ExtDTrxop=None, cancelled_by: ExtDTrxop=None, execution_irreversible: bool=None,
                 creation_irreversible: bool=None, cancellation_irreversible: bool=None):
        self.transaction_status = transaction_status
        self.transaction = transaction
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
