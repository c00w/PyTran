from decorator import event
from sys import stdin

@event(stdin)
def test(ce, data):
    print data
    return ce
