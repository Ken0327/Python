import sys

class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None

def del_node(head, ptr):
    top = head
    if ptr.num == head.num: # if delete head of list
        head = head.num
        print('Deleted No.%d employee name:%s salary:%d' %(ptr.num, ptr.name, ptr.salary))
    else:
        while top.next != ptr: # find position before deleted
            top = top.next
        if ptr.next == None: # delete last of list
            top.next = None
            print('Deleted No.%d employee name:%s salary:%d' %(ptr.num, ptr.name, ptr.salary))
        else:
            top.next = ptr.next # Deleted node of list
            print('Deleted No.%d employee name:%s salary:%d' %(ptr.num, ptr.name, ptr.salary))
    return head

def main():
    position = 0
    data = [
        [1001, 32346], [1002, 24388], [1003, 23446], [1007, 32458], [1014, 43267], [1025, 51492]
    ]
    namedata = [
        'Allen', 'Scott', 'Marry', 'John', 'Mark', 'Cathy'
    ]

    print('EmplyeeNo  Salary')
    print('--------------------------------------------')
    for i in range(6):
        print('[%4d] $%5d' %(data[i][0], data[i][1]))
    print('--------------------------------------------')

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

    while(True):
        print('Please input employee No. you want to delete. Input -1 to exit ')
        position = int(input('Input No: '))
        if position == -1:
            break
        else:
            ptr = head
            find = 0
            while ptr != None:
                if ptr.num == position:
                    ptr = del_node(head, ptr)
                    find +=1
                    head = ptr
                ptr = ptr.next
            if find == 0:
                print('######## Not found ########')

    ptr = head
    print('\t Emploee No. \t Name \t Salary')
    print('-----------------------------------------')
    while ptr != None:
        print('\t[%2d]\t[%-7s]\t[%3d]' %(ptr.num, ptr.name, ptr.salary))
        ptr = ptr.next

main()