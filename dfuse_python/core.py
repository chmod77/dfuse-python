#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import json
import os
import sqlite3
import tempfile
from sqlite3 import Error
from typing import Any, Dict, Sequence

import requests
import requests_cache
from decouple import config
import datetime


class Dfuse:
    _session = None
    __DEFAULT_BASE_URL: str = ""
    __DEFAULT_TIMEOUT: int = 30
    __TEMPDIR_CACHE: bool = True
    def __UNIXTIMESTAMP(n): return datetime.datetime.fromtimestamp(n)  # TO-USE
    __BLOCK_TIME_URL: str = 'https://mainnet.eos.dfuse.io/v0/block_id/by_time'
    __API_KEY: str = config('API_KEY')
    __DB_NAME: str = 'dfusepy.sqlite3'
    __CREATE_TBL_SQL = """
                    CREATE TABLE IF NOT EXISTS tokens (token TEXT, 
                    created TIMESTAMP)
                    """

    __INSERT_TOKEN_SQL = """ INSERT INTO tokens(token,created) VALUES(?,?) 
                        """

    def __init__(
        self,
        api_key: str = _Dfuse__API_KEY,
        base_url: str = _Dfuse__DEFAULT_BASE_URL,
        request_timeout: int = _Dfuse__DEFAULT_TIMEOUT,
        tempdir_cache: bool = _Dfuse__TEMPDIR_CACHE,
        block_by_time_url: str = __BLOCK_TIME_URL,
        db_name: str = _Dfuse__DB_NAME,
        token: str = '',
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.cache_filename = "dfuse_python.cache"
        self.db_name = db_name
        self.token = None
        self.cache_name = (
            os.path.join(tempfile.gettempdir(), self.cache_filename)
            if tempdir_cache
            else self.cache_filename
        )
        self.get_auth_token()

    @property
    def session(self) -> Any:
        if not self._session:
            self._session = requests_cache.CachedSession(
                cache_name=self.cache_name, backend="sqlite", expire_after=120
            )
            self._session.headers.update({"Content-Type": "application/json"})
            self._session.headers.update({'User-agent': 'dfusepython - python wrapper around \
                                            dfuse.io'})
        return self._session

    def __request_get(self, endpoint, params):
        """
        TO-USE
        """
        response_object = self.session.get(
            endpoint, params=params, timeout=self.request_timeout)

        try:
            response = json.loads(response_object.text)
            if isinstance(response, list) and response_object.status_code == 200:
                response = [
                    dict(item, **{'cached': response_object.from_cache}) for item in response]
            if isinstance(response, dict) and response_object.status_code == 200:
                response['cached'] = response_object.from_cache
        except Exception as e:
            return e
        return response

    def __request_post(self, endpoint, data):
        """
        TO-USE
        """
        response_object = self.session.post(
            endpoint, json=data, timeout=self.request_timeout)
        try:
            response = json.loads(response_object.text)
            if isinstance(response, list) and response_object.status_code == 200:
                response = [
                    dict(item, **{'cached': response_object.from_cache}) for item in response]

            if isinstance(response, dict) and response_object.status_code == 200:
                response['cached'] = response_object.from_cache
        except Exception as ex:
            return ex
        return response

    def create_connection(self, db_file=_Dfuse__DB_NAME):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)

    def create_table(self, conn, sql: str = _Dfuse__CREATE_TBL_SQL):
        """ create a table from the sql statement
        :param conn: Connection object
        :param sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)
        finally:
            conn.close()

    def insert_token(self, conn, data):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """

        cur = conn.cursor()
        cur.execute("INSERT INTO tokens(token,created) VALUES(?,?)", data)
        print('Inserting')
        return cur.lastrowid

    def drop_entries(self, conn):
        if conn:
            sql = 'DELETE FROM tokens'
            cur = conn.cursor()
            cur.execute(sql)

    def save_token_to_db(self):
        conn = self.create_connection()
        if conn is not None:
            # Delete any present entry
            self.drop_entries(conn)
            self.create_table(conn)
            self.insert_token(conn)
        else:
            print(f'Failed to connect to db {self.db_name}')

    def check_token_expiry(self):
        conn = self.create_connection()
        if conn is not None:
            ...

    def read_token(self, conn):
        """
        Query all rows in the token table
        :param conn: the Connection object
        :return:
        """


        cur = conn.cursor()

        cur.execute("SELECT * FROM tokens")

        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print('Nothing in db.')

    def get_auth_token(self):
        """
        Obtains a short term (24HRS) token

        TODO - cache token for < 24 hrs to avoid rate limits.
        TODO - Check for token in db. Expired? Fetch from API. Rewrite to capture this.

        """
        # Read token from db
        conn = self.create_connection()
        if conn:
            try:
                self.read_token(conn)
            except sqlite3.OperationalError:
                self.create_table(conn)

        if not self.token:
            r = requests.post('https://auth.dfuse.io/v1/auth/issue', json={
                'api_key': self.api_key}, headers={'Content-Type': 'application/json'})
            try:
                token = r.json().get('token')
            except Exception as e:
                raise Exception(
                    f'Failed with status {r.status} and reason {r.json().get("reason")}')
            self.token = token
            conn = self.create_connection()
            if conn:
                data = (token, datetime.datetime.now())
                self.insert_token(conn, data)
                self.read_token(conn)
            return self.token
        return self.token

    # REST

    def get_block_at_timestamp(self, time, comparator='gte'):
        '''
        (Beta) GET /v0/block_id/by_time/by_time?time=2019-03-04T10:36:14.5Z&comparator=gte: Get the block ID produced at a given time

        Response:
        ```
        {
            "block": {
                "id": "02bb43ae0d74a228f021f598b552ffb1f8d2de2c29a8ea16a897d643e1d62d62",
                "num": 45826990,
                "time": "2019-03-04T10:36:15Z"
            }
        }
        ```
        '''
        ...

    def get_transaction_lifecycle(self, id: str):
        '''
        (Beta) GET /v0/transactions/:id: Fetching the transaction lifecycle associated with the provided path parameter :id.

        https://mainnet.eos.dfuse.io/v0/transactions/1d5f57e9392d045ef4d1d19e6976803f06741e11089855b94efcdb42a1a41253
        '''
        ...

    def fetch_abi(self, account: str, json: bool = True):
        '''
        (Beta) GET /v0/state/abi: Fetch the ABI for a given contract account, at any block height.

        https://mainnet.eos.dfuse.io/v0/state/abi?account=eosio&json=true
        '''
        ...

    """
    POST https://auth.dfuse.io/v1/auth/issue: Exchange a long-term API key for a short-lived (24 hours) API Authentication Token (JWT).

    



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
