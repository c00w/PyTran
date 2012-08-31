from decorator import event
from sys import stdin
from StringIO import StringIO
from time import sleep

def test_ce_writing():
    buffer1 = StringIO()
    buffer2 = StringIO()
    buffer1.write('a')
    @event(buffer1)
    def func1(ce, data):
        ce['d'] = data
        return ce


    sleep(0)
    buffer2.write('a')
    @event(buffer2)
    def func2(ce, data):
        assert ce['d'] == 'a'
        return ce
    sleep(0)   
