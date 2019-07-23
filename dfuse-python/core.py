#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import tempfile

import requests
import requests_cache

from typing import Any

class Dfuse:
    _session = None
    __DEFAULT_BASE_URL = ''
    __DEFAULT_TIMEOUT = 30
    __TEMPDIR_CACHE = True

    def __init__(self, api_key: str, base_url=_Dfuse__DEFAULT_BASE_URL, request_timeout=_Dfuse__DEFAULT_TIMEOUT, tempdir_cache=_Dfuse__TEMPDIR_CACHE):
        self.api_key = api_key
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.cache_filename = 'dfuse_python.cache'
        self.cache_name = os.path.join(tempfile.gettempdir(
        ), self.cache_filename) if tempdir_cache else self.cache_filename

    @property
    def session(self) -> self._session:
        if not self._session:
            self._session = requests_cache.CachedSession(
                cache_name=self.cache_name, backend='sqlite', expire_after=120)
            self._session.headers.update({'Content-Type': 'application/json'})
        return self._session

    # REST


    # WEBSOCKETS


    # GRAPHQL via grpc
