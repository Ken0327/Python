# import threading
# import time
# def hello():
#     print("hello, world")

# print('Start')
# t = threading.Timer(2.0, hello)
# t.start()
# time.sleep(5)
# t.cancel()
# print('Finished')

# -------------------------------------------------------------------
from threading import Timer
import time

class RepeatableTimer(object):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs
    def start(self):
        t = Timer(self._interval, self._function, *self._args, **self._kwargs)
        t.start()

def hello():
    print "hello"

a=RepeatableTimer(3,hello,())
a.start()
time.sleep(4)
a.start()