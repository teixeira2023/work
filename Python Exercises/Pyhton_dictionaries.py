person1 = {"name":"Alan","age":44}
print(person1)#variável que contém a lista com {key:value}
print(person1["name"])#exibe o value da key
print(person1["age"])#exibe o value da key
print(person1.get("hobbies"))#get procura a key hobbies na lista
print(person1.get("age"))
person2 = {"name":" ","age":" ","hobbie":" "}
person2["name"] = "João" #adiciona key e value
person2["age"] = "54"
person2["hobbie"] = ["phishing","dancing"]
                     
print(person2)
for key in person2:
    print(key)
    print(person2[key])


person2.pop("hobbie")#deleta key
print(person2)