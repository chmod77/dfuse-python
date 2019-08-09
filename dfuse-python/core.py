#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import tempfile

import requests
import requests_cache

import datetime
from typing import Any


class Dfuse:
    _session = None
    __DEFAULT_BASE_URL = ""
    __DEFAULT_TIMEOUT = 30
    __TEMPDIR_CACHE = True
    __UNIXTIMESTAMP = lambda n: datetime.datetime.fromtimestamp(n)

    def __init__(
        self,
        api_key: str,
        base_url=_Dfuse__DEFAULT_BASE_URL,
        request_timeout=_Dfuse__DEFAULT_TIMEOUT,
        tempdir_cache=_Dfuse__TEMPDIR_CACHE,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.cache_filename = "dfuse_python.cache"
        self.cache_name = (
            os.path.join(tempfile.gettempdir(), self.cache_filename)
            if tempdir_cache
            else self.cache_filename
        )

    @property
    def session(self) -> self._session:
        if not self._session:
            self._session = requests_cache.CachedSession(
                cache_name=self.cache_name, backend="sqlite", expire_after=120
            )
            self._session.headers.update({"Content-Type": "application/json"})
        return self._session

    def get_auth_token(self):
        """
        Obtains a short term (24HRS) token

        TODO - cache token for < 24 hrs to avoid rate limits.
        """

        r = requests.post('https://auth.dfuse.io/v1/auth/issue', json={'api_key': self.api_key}, headers = {'Content-Type':'application/json'})
        try:
            token = r.json().get('token')
        except Exception as e:
            raise Exception(f'Failed with status {r.status} and reason {r.json().get('reason')}')    
        return token

    # REST
    """
    POST https://auth.dfuse.io/v1/auth/issue: Exchange a long-term API key for a short-lived (24 hours) API Authentication Token (JWT).

    (Beta) GET /v0/block_id/by_time: Get the block ID produced at a given time

    (Beta) GET /v0/transactions/:id: Fetching the transaction lifecycle associated with the provided path parameter :id.

    (Beta) GET /v0/state/abi: Fetch the ABI for a given contract account, at any block height.

    (Beta) POST /v0/state/abi/bin_to_json: Decode binary rows (in hexadecimal string) for a given table against the ABI of a given contract account, at any block height.

    (Beta) GET /v0/state/permission_links: Fetching snapshots of any account’s linked authorizations on the blockchain, at any block height.

    (Beta) GET /v0/state/table: Fetching snapshots of any table on the blockchain, at any block height.

    (Beta) GET /v0/state/table/accounts: Fetching snapshots of any table on the blockchain, at any block height, for a list of accounts (contracts).

    (Beta) GET /v0/state/table/scopes: Fetching snapshots of any table on the blockchain, at any block height, for a list of scopes for a given account (contract).

    (Beta) GET /v0/search/transactions: Structure Query Engine (SQE), for searching the whole blockchain history and get fast and precise results.

    (Beta) POST /v1/chain/push_transaction: Drop-in replacement for submitting a transaction to the network, but can optionally block the request until the transaction is either in a block or in an irreversible block.

    Other /v1/chain/...: Reverse-proxy of all standard chain requests to a well-connected node.
    """

    # WEBSOCKETS
    """
    type	string	required	The type of the message. See request types below.
    data	object	required	A free-form object, specific to the type of request. See request types below.
    req_id	string	optional	An ID to associate responses back with the request
    start_block	number (integer)	optional	Block at which you want to start processing. It can be an absolute block number, or a negative value, meaning how many blocks from the current head block on the chain. Ex: -2500 means 2500 blocks in the past, relative to the head block. 0 means the beginning of the chain. See Never missing a beat
    irreversible_only	boolean	optional, defaults to false	Limits output to events that happened in irreversible blocks. Only supported on get_action_traces
    fetch	boolean	optional, defaults to false	Whether to fetch an initial snapshot of the requested entity.
    listen	boolean	optional, defaults to false	Whether to start listening on changes to the requested entity.
    with_progress	number (integer)	optional	Frequency of the progress of blocks processi
    """

    # GRAPHQL via grpc
