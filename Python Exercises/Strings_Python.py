

def greet():
    print("""You can just
keep typing in a 
paragraph!
In the same print!!!!""")
    
    
greet()

text = "And, as they said \"you won\'t need to care with these quotation marks and apostrophe\""

print(text)
print(text[0:33])

text1 = "Python"
text2 = "Programming"
result = text1 + " " + text2 #concatena 2 textos
print(result)
multiplyText = result*4 #multiplica strings
print(multiplyText)
for character in text1:
    print(character)
print(len(text1))
print("onx"in text1)#verifica se caracteres estão no texto
print("on"in text1)
text3 = "HI, HELLO"
print(text3)
result = text3.lower()
print("texto  com o lower direto: ",text3.lower(),"texto com o lower através de uma variável: ",result)
print(text.upper())
result2 = text.find("quotation")
print(result2)
text4 = "I love Python"
result3 = text4.replace("Pyhton", "Javascript")
print(text4.replace("Pyhton", "Java"),result3)
quote = "Talk is cheap.Show me the code"
print("1.",quote[3])
print("2.",quote[-3])
print("3.",quote.replace("code","program"))
