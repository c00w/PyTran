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


    sleep(0)
    buffer2.write('a')
    @event(buffer2)
    def func2(ce, data):
        assert ce['d'] == 'a'
    sleep(0)   


def test_gen():
    def test_func():
        yield 'test'
        yield 'test'
        yield 'end'

    i = 3 

    @event(test_func())
    def func3(ce, data):
        i -= 1
        if 'data' == 'end':
            assert ce['done'] == True
            return
        if ce['flag'] != True:
            ce['flag'] == True
        else:
            ce['done'] = True
        if i == 0:
            assert False
