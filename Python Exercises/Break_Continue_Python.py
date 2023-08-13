'''for item in range(1,11):
    if item  == 5:
        print(item)
        break
print(item, "\nthe end")'''

'''while True:
   number = float(input("Enter a number: "))
   if number < 0:
       break #interrompe o codigo assim que a condição é verdadeira
   print("You entered: ",number)'''
   
'''for i in range(10):
    number = float(input("enter a number: "))
    
    if number < 0:
        continue #pula os negativos e continua a sequencia de 10 numeros
    print(number)'''
    
languages = ["Python","Java","Swift","C","C++"]

for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)
 