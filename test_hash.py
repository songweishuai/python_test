#!/usr/bin/python3
# -*- utf-8 -*-

import hashlib
import logging

# print(hashlib.md5("cache_ktvinfo_123456789").)
print("hello world")

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    key = hashlib.md5("cache_ktvinfo_123456789".encode("utf-8")).hexdigest().upper()
    print(key)
    print(logging.getLogger(__name__))
    logger.error('exit')
