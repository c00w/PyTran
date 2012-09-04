from threading import current_thread, Thread
from copy import copy
import ce

def call_func(func, data):
    new_ce = ce.get()
    func(new_ce, data)
    return ce.update(new_ce)

def handle_message(func, message):
    while not call_func(func, message):
        pass

def listen(func, gen):
    while True:
        for item in gen:
            handle_message(func, item)

def event(gen, size=1):
    def decorator(func):
        t = Thread(target=listen, args = (gen, func))
        t.daemon = True 
        t.start()
    return decorator
