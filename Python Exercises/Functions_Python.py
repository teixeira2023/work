'''def greet():
    print("Hello")
    
number = input("enter a input: ") 
if number.lower() == "hi":
    greet()
else:
    print("end")
    #break'''
 
    
'''def greet(name):
    print("Hello",name) #qdo a função é executada, o texto é recebido pela variável 
    print("How do you do?")
    #print(name) mostra o valor que foi atribuido na execução da função

greet("Jack") #o nome jack é atribuido a variável name'''
 
'''def add_number(n1,n2):
    result = n1 + n2
    print("The sum is", result)


number1 = 5
number2 = 10
add_number(number1,number2)'''

###USING THE RETURN STATEMENT
'''def add_number(n1,n2):
    result = n1 + n2
    return result


number1 = 5
number2 = 10
result = add_number(number1,number2)
print("The sum is", result)'''

### CALCULATE SPEED SLOTS AND THE AVERAGE SPEEDS USING FUNCTION ###
'''def calculate(marks,lenght):
    
    marks_mean = sum(marks)/lenght
    
    return marks_mean
 
marks = [55,65,75,85,93]
lenght = len(marks)
marks_sum = sum(marks)
marks_mean = calculate(marks,lenght)

print("The speed slots that must be logged are: ",marks,"in a total of",lenght, "speed slots")
print("The average speed is equal to: ",marks_mean,"Km/h")'''

### Calculate average marks and grade using functions ###
'''def average_marks(marks,lenght):
    mean = sum(marks)/lenght
    return mean
    
marks = [95,64,75,80,95]
lenght = len(marks)
mean = average_marks(marks,lenght)

if mean >= 80:
    print("Your average mark is: ",mean,"and you get Grade A. Congrats!!!")
elif mean >= 60 and mean < 80:
    print("Your average mark is: ",mean,"and you get Grade B.")
elif mean >= 50 and mean< 60:
    print("Your average mark is: ",mean,"and you get Grade C.")
else:
    print("Your average mark is: ",mean,"and you get Grade F.")'''



# function to find average marks
'''def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks
        
# Calculate the grade and return it 
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55,65,75,85,95]
average_marks = find_average_marks(marks)
print("Your average marks is:", average_marks)
grade = compute_grade(average_marks)
print("Your grade is:", grade)'''

def add_numbers(num1,num2):
    add = num1 + num2
    return add

def multiply_numbers(num1,num2):
    multi = num1 * num2
    return multi

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
add = add_numbers(number1,number2)
multi = multiply_numbers(number1,number2)
print("add:",add,"\nmultiplication",multi)

        