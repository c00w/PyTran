from copy import copy
from threading import Lock

ce = {}
lock = Lock()

def get():
    return copy(ce)

def update(old_ce, new_ce):
    # In some cases this is an incorrect result
    # Here for rapid prototyping
    if old_ce != ce:
        return False
    if old_ce == ce and new_ce != old_ce:
        with lock:
            for x in new_ce.iterkeys():
                if new_ce[x] != old_ce[x]:
                    ce[x] = new_ce[x]
    return True
