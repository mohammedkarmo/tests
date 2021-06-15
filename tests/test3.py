class student :
    counter = 0
    def __init__(self):
        student.counter +=1
    def func1(self):
        print(student.counter)
s1=student()
s1.func1()
s2=student()
s2.func1()
s3=student()
s3.func1()