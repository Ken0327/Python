'''
*args是可变的positional arguments列表，**kwargs是可变的keyword arguments列表。

*args必须位于**kwargs之前，因为positional arguments必须位于keyword arguments之前。
'''

def test_args(first, *args):
   print 'Required argument: ', first
   for v in args:
      print 'Optional argument: ', v

test_args(1, 2, 3, 4)

'''
def test_kwargs(first, *args, **kwargs):
       print 'Required argument: ', first
   for v in args:
      print 'Optional argument (*args): ', v
   for k, v in kwargs.items():
      print 'Optional argument %s (*kwargs): %s' % (k, v)

test_kwargs(1, 2, 3, 4, k1=5, k2=6)
'''