from copy import copy
from threading import Lock
from collections import defaultdict
from pprint import pprint

ce = defaultdict(lambda: None) 
lock = Lock()

def good_base_ce(old_ce, new_ce):
    for item in new_ce:
        if new_ce[item] != old_ce[item]:
            if old_ce[item] != ce[item]:
                return False
    return True

def get():
    return copy(ce)

def update(old_ce, new_ce):
    # In some cases this is an incorrect result
    # Here for rapid prototyping
    if not good_base_ce(old_ce, new_ce):
        return False
    if old_ce == ce and new_ce != old_ce:
        with lock:
            for x in new_ce.iterkeys():
                if new_ce[x] != old_ce[x]:
                    ce[x] = new_ce[x]
    return True
