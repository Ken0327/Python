import sys


class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None


def invert(x):
    p = x  # p point to head of list
    q = None  # q is the node before p
    while p != None:
        r = q  # put r after q
        q = p  # put q after p
        p = p.next  # p move to next node
        q.next = r  # q links to previous node
    return q


def main():
    position = 0
    data = [
        [1001, 32346], [1002, 24388], [1003, 23446], [
            1007, 32458], [1014, 43267], [1025, 51492]
    ]
    namedata = [
        'Allen', 'Scott', 'Marry', 'John', 'Mark', 'Cathy'
    ]

    # head of list
    head = employee()
    head.next = None

    if not head:
        print('Error! memory configuration fail')
        sys.exit(1)

    head.num = data[0][0]
    head.name = namedata[0]
    head.salary = data[0][1]
    head.next = None
    ptr = head
    for i in range(1, 6):
        newnode = employee()
        newnode.next = None
        newnode.num = data[i][0]
        newnode.salary = data[i][1]
        newnode.name = namedata[i]
        ptr.next = newnode
        ptr = ptr.next

    # original list
    ptr = head
    i = 0
    print('Original list')
    while ptr != None:
        print('[%2d %6s %3d] => ' % (ptr.num, ptr.name, ptr.salary), end='\t')
        i += 1
        if i >= 3:
            print()
            i = 0
        ptr = ptr.next

    # invert list
    ptr = head
    before = None
    before = invert(ptr)
    ptr = before

    print('Invert list')
    while ptr != None:
        print('[%2d %6s %3d] => ' % (ptr.num, ptr.name, ptr.salary), end='\t')
        i += 1
        if i >= 3:
            print()
            i = 0
        ptr = ptr.next


main()
