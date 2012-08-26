from decorator import event
from sys import stdin

@event(stdin)
def test(data):
    print data
