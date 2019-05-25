import sys

class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None

def findnode(head, num):
    ptr = head
    while ptr != None:
        if ptr.num == num:
            return ptr
        ptr = ptr.next
    return ptr

def insertnode(head, ptr, num, salary, name):
    insertNode = employee()
    if not insertNode:
        return None
    insertNode.num = num
    insertNode.salary = salary
    insertNode.name = name
    insertNode.next = None
    if ptr == None: # insert into head of list
        insertNode.next = head
        return insertNode
    else:
        if ptr.next == None: # insert into last of list
            ptr.next = insertNode
        else:   # insert into middle of list
            insertNode.next = ptr.next  # ?
            ptr.next = insertNode
    return head

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
    print('Please input employee No. after inserting employee No. \
        If No. is not in list, new No. will be head of list. Input -1 to exit ')
    position = int(input('Input No: '))
    if position == -1:
        break
    else:
        ptr = findnode(head, position)
        new_num = int(input('Please input inserting employee No: '))
        new_salary = int(input('Please input inserting employee salary: '))
        new_name = input('Please input inserting employee name: ')
        head = insertnode(head, ptr, new_num, new_salary, new_name)
    print()

ptr = head
print('\t Emploee No. \t Name \t Salary')
print('-----------------------------------------')
while ptr != None:
    print('\t[%2d]\t[%-7s]\t[%3d]' %(ptr.num, ptr.name, ptr.salary))
    ptr = ptr.next