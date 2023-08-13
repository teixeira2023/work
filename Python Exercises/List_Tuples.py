# a list of integrers
numbers = [1,2,3,4,5] #cria a lista
print(len(numbers)) #retorna o numero de itens
#empty list
list1 = []#lista vazia
print(len(list1))#retorna o numero de itens, nesse caso 0
print(list1)
print(numbers[2])# exibe o index 2 da lista -->[0,1,2,3,4]<--index
print(numbers[-4])#retorna o item de tras pra frente, no caso o quarto item e não o index
print(numbers[0:5])#retorna o [index : item(coluna)]
languages = ["Python","Javascript","C++","Kotlin"]
print(languages)
languages[1] = "Ruby" #troca o index da lista 
print(languages)
print("C#" in languages)#verifica se o text está contido na lista
print("C++" in languages)
languages[2:4] = ["HTML","CSS"]#troca informação em[index,item]
print(languages)
languages.append("Alan")#adiciona ao final da lista
print(languages)
languages.insert(4,"Matlab")#insere o valor no index 4
print(languages)
newLanguages = languages.copy()#copia a lista em uma variável 
print("The new list os languages is:",newLanguages)
newLanguages.remove("Alan")#remove itens de uma lista
print(newLanguages)
newLanguages2 = ("A","B","C","D","E") #atribui uma variável a outra
print("This is still a list:",newLanguages)
print("This is a Tuple:",newLanguages2[0:5])
'''### REMOVER O COMMENT PARA RODAR O ERRO DO TUPLE ###
newLanguages2.append("Alan")#tuple não permite ser editada
print(newLanguages2)'''
