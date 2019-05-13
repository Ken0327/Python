import re

class Check(object):
    def __init__ (self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.temp = self.kwargs['temp']
        self.settemp = self.kwargs['settemp']


    def __call__(self, func):
        def newfunction(*args, **kwargs):
            print 'call %s():' % func.__name__
            if self.temp < self.settemp:
                print 'Turn On'
                ret = func(*args, **kwargs)
            else:
                print 'Turn Off'
                ret = func(*args, **kwargs)
            return ret
        newfunction.__doc__ = func.__doc__
        return newfunction 
    