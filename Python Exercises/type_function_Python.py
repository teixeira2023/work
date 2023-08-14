### TIPOS DE CLASSES ###
numbers = [1,4,9,16]
print(type(numbers))
print(dir(numbers)) #mostra todos os atributos que podem ser utilizados
### <class 'list'> ###
n1 = 5
print(type(n1))
### <class 'int'> ###
flag = True
print(type(flag))
### <class 'bool'> ###
def my_function():
    pass

print(type(my_function))
### <class 'function'> ###

number_list = [1, 2]
result = number_list.__add__([3,4])
print(result)
result = number_list + [3,4]
print(result)

number1 = 5
print(id(number1))#mostra o id do valor atribuido
number2 = 10
print(id(number2))

a = [1,2,3]#cria uma lista e atribui para a
b = a#atribui os valores de a para b. ambos vão se referir ao mesmo objeto
a.append(4)#adiciona o valor a lista
print("a = ",a)
print("b = ",b)# o valor atribuido em a aparece em b por estarem referenciados ao mesmo objeto

a = [1,2,3]#cria uma lista e atribui para a
b = a.copy()#copia os valores de a para b. mas não estão associados ao mesmo objeto
a.append(4)#adiciona o valor a lista a
print("a = ",a)
print("b = ",b)# o valor atribuido nãoaparece em b por não estarem referenciados ao mesmo objeto