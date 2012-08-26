from input import Input
from threading import current_thread, Thread

def listen(socket, func):
    while True:
        data = socket.read(current_thread())
        func(data)

def event(socket, size=1):
    def decorator(func):
        item = Input(socket, size)
        t = Thread(target=listen, args = (item, func))
        t.daemon = False
        t.start()
    return decorator
