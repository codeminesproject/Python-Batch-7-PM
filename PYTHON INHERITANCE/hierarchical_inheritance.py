
class Institute:
    def institutedetails(self):
        print("Name: CodeMines Computer Institute")
        print("Mobile: 9167519953")
        print("Email: santtoshupadhyay@gmail.com")

class Student(Institute):
    def studentdetails(self):
        print("Name: Student Name")


class Teacher(Institute):
    def teacherdetails(self):
        print("Name: Teacher Name")

objStudent = Student()
objStudent.studentdetails()
objStudent.institutedetails()

objTeacher = Teacher()
objTeacher.teacherdetails()
objTeacher.institutedetails()