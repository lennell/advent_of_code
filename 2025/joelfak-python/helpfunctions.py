#!/usr/bin/env python3

from functools import wraps
from time import time
from typing import Generator

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('Execution of:%r took: %2.4f sec' % \
          (f.__name__, te-ts))
        return result
    return wrap

def readFile(filename) -> Generator[str, None, None]:
    with open(filename) as file:
        while True:
            data = file.readline()
            if not data:
                break
            yield data.strip()
