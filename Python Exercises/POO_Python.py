class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = student()
student1.name = "Harry"
student1.marks = 85

student2 = student()
student2.name = "Janete"
student2.marks = 35


did_pass = student2.check_pass_fail()
print(student2.name)
print("The student: ",student2.name,"The marks = ",student2.marks)
if did_pass == True:
    print("You have passed the exam!!! Congratulations!!!")
else:
    print("You don\'t have passed the exam")