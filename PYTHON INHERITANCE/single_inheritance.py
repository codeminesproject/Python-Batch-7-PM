class Institute:
    def institutedetails(self):
        print("Name: CodeMines Computer Institute")
        print("Mobile: 9167519953")
        print("Email: santtoshupadhyay@gmail.com")

class Student(Institute):
    def studentdetails(self):
        print("Name: Student Name")

# student will access all private properties of Institute Class
# In inheritance we always create object of child class

obj_Student = Student()
obj_Student.institutedetails()
obj_Student.studentdetails()
