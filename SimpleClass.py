from _datetime import datetime
from test.pyclbr_input import Other
class Student1:
    rollNoUpdate = 1
    noOfStudentz = 0
    def __init__(self, firstName,lastName,rollNo):
        self.firstName = firstName
        self.lastName = lastName
        self.rollNo = rollNo
        Student1.noOfStudentz = Student1.noOfStudentz + 1
        
    def __repr__(self):  #we can change how object will be printed
        return "Student1('{}' , '{}' , '{}' )".format(self.firstName,self.lastName,self.rollNo)
    
    def __str__(self):   # we can change how object will be printed
        return "Student1('{}' '{}' - '{}'  )".format(self.firstName,self.lastName,self.rollNo)
     
    def __add__(self,other):
        return self.rollNo + other.rollNo
         
        
    def fullName(self):
        print('{} {}'.format(self.firstName, self.lastName))

    def updateRollNo(self):
        self.rollNo = self.rollNo + Student1.rollNoUpdate
        
    @classmethod
    def set_raise_rollno(cls, number):
        cls.rollNoUpdate = number
    @staticmethod
    def schoolHoliday(day):
        if (day.weekday() == 5):
            print("Holiday")
        else:
            print("not")
        
stu_1 = Student1("ABC", "def", 12)
stu_2 = Student1("DFSF", "deDSFSF", 120)
print(stu_1)
print(stu_1+stu_2)
stu_1.fullName()
stu_2.fullName()
print(stu_1.rollNo)
print("")
stu_1.updateRollNo()
print("Student1 roll number ", stu_1.rollNo)
print("")
print("Everything in stu1 object",stu_1.__dict__)
print("")
print("Everything in Student1 Class",Student1.__dict__)
print("")
Student1.set_raise_rollno(100)
print("")
print("Student 1 roll number update",stu_1.rollNoUpdate)
print("Student 2 roll number update",stu_2.rollNoUpdate)
print("")
print("No of Students in Student1 Class",Student1.noOfStudentz)
#datetime is imported here 
import datetime
d = datetime.date(2018, 9,22)
Student1.schoolHoliday(d)

class WorkingStudent(Student1):
    pass

