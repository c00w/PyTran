from input import Input
from threading import current_thread, Thread
from copy import copy
import ce

def call_func(func, data):
    old_ce = ce.get() 
    new_ce = func(copy(old_ce), data)
    return ce.update(old_ce, new_ce)

def listen(socket, func):
    while True:
        data = socket.read(current_thread())
        if call_func(func, data):
            socket.commit(current_thread())
        else:
            socket.cancel(current_thread())

def event(socket, size=1):
    def decorator(func):
        item = Input(socket, size)
        t = Thread(target=listen, args = (item, func))
        t.daemon = False
        t.start()
    return decorator
