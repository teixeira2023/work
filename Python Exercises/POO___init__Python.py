'''class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
        
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
        

student1 = student("Harry",85)
student2 = student("Janete",95)


did_pass = student1.check_pass_fail()
print(student1.name)
print("The student: ",student1.name,"The marks = ",student1.marks)
if did_pass == True:
    print("You have passed the exam!!! Congratulations!!!")
else:
    print("You don\'t have passed the exam")
    
did_pass = student2.check_pass_fail()
print(student2.name)
print("The student: ",student2.name,"The marks = ",student2.marks)
if did_pass == True:
    print("You have passed the exam!!! Congratulations!!!")
else:
    print("You don\'t have passed the exam")'''
    
#### COMPLEX NUMBERS ####

'''class complex:         #create class
    def __init__(self,real,imag):
        self.real = real 
        self.imag = imag
        
    def add(self,number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = complex(real,imag)
        return result

    
     
        
n1 = complex(5,6) ##create 2 comlex numbers
n2 = complex(-4,2)
result = n1.add(n2)
print("real =",result.real)
print("imag =",result.imag)'''

### CLASS TRIANGLE ###

class triangle:         #create class
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        pass
        
    def perimiter(self):
        trianglePerimiter = self.a + self.b + self.c
        return trianglePerimiter

    
     
        
t1 = triangle(3,4,5)
trianglePerimiter = t1.perimiter()
 
print("The triangle perimiter is =",trianglePerimiter)
 