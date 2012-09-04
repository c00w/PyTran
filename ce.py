from copy import copy
from threading import Lock
from collections import defaultdict
from pprint import pprint

lock = Lock()

class CE():
    index = 0
    data = defaultdict(lambda: None) 
    new_data = defaultdict(lambda: None) 

    def __get__(self, key):
        if key in self.new_data:
            return self.new_data[value]
        return self.data[key]

    def __set__(self, key, value):
        self.new_data[key] = value

    def __delete__(self, key):
        self.new_data[key] = None
    
    def commit(self):
        self.data = new_data
        self.new_data = defaultdict(lambda: None) 
        index += 1

    def changed(self):
        return self.new_data.keys()

ce = CE()

def good_base_ce(new_ce):
    for item in new_ce.changed():
        if new_ce.data[item] != ce[item]:
            return False
    return True

def get():
    return copy(ce)

def update(new_ce):
    if not good_base_ce(new_ce):
        return False
    if new_ce.changed():
        with lock:
            for x in new_ce.new_data.iterkeys():
                    ce[x] = new_ce[x]
            ce.commit()
    return True
