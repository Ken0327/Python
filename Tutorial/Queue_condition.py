import collections
import threading
import time

queue = collections.deque()
condition = threading.Condition()

def consumer():
    condition.acquire()
    while True:
        while queue:
            item = queue.popleft()
            condition.release()
            # do something with item
            print(item)
            condition.acquire()
        condition.wait()

def push_item(item):
    with condition:
        queue.append(item)
        condition.notify()

# From that point forward, it is just demonstration code to show how to use

def example_producer_thread(*args):
    for arg in args:
        push_item(arg)

consumer_thread = threading.Thread(target=consumer, name='queue consumer')
consumer_thread.daemon = True  # so it does not prevent python from exiting
consumer_thread.start()

for example in [range(0, 10), range(10, 20), range(20, 30)]:
    threading.Thread(target=example_producer_thread, args=example).start()

time.sleep(1) # let the consumer thread some time before the script gets killed