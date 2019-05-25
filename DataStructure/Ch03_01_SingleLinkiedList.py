
class student():
    def __init__(self):
        self.name = ''
        self.Math = 0
        self.Eng = 0
        self.no = ''
        self.next = None

head = student()
head.next = None
ptr = head
select = 0
MathSum = EngSum = student_no = 0

while select != 2:
    print('(1)New (2)Exit =>')
    try:
        select = int(input('Choose a option please:'))
    except ValueError:
        print('input error, please type again')
    if select == 1:
        new_data = student()
        new_data.name = input('Name:')
        new_data.no = input('No:')
        new_data.Math = eval(input('Math:'))
        new_data.Eng = eval(input('English:'))
        new_data.next = None
        ptr.next = new_data
        ptr = ptr.next

ptr = head.next
print()

while ptr != None:
    print('Name: %s\t No: %s\t Math score: %s\t English score: %s\t' \
        %(ptr.name, ptr.no, ptr.Math, ptr.Eng))
    MathSum += ptr.Math
    EngSum += ptr.Eng
    student_no += 1
    ptr = ptr.next

if student_no != 0:
    print('-------------------------------')
    print('Average score of students in Math: %.2f English: %2f' \
        %(MathSum/student_no, EngSum/student_no))