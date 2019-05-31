class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None

def invert(x):
    p = x # p point to head of list
    q = None # q is the node before p
    while p != None:
        r = q # put r after q
        q = p # put q after p
        p = p.next # p move to next node
        q.next = r # q links to previous node
    return q 

