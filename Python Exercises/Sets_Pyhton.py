#animals = {"dog","cat","tiger","elephant"} set criado usando chaves e separado por virgula
#animals = {"dog","cat","tiger","elephant","dog"} itens repetidos não são mostrados
animals = set(["dog","cat","tiger","elephant"]) #retorna um set convertendo a lista em set
print(animals)
animals.add("monkey") #adiciona monkey ao set animals
print(animals)
wild_animals = ["tiger","leopard","elephant"]
animals.update(wild_animals,{"dolphins"})#adiciona a lista ao set animals
print("Wild animals and dolphin added in the set animals: ",animals)
animals.discard("cat")#descarta o valor mencionado
print("The set with cat discarded: ",animals)
animals2 = animals.copy()#copia o set em uma outra variável
print(animals2)
animals2.clear()#limpa o conteúdo do set
print(animals)
print("The set cleared is: ",animals2,"\nreturn true when the item is available in the set: ", "tiger" in animals,"\nreturn false when the item is not in the set: ","ferret" in animals)
for animal in animals:
    print(animal)


domestic_animals = {"dog","cat","elephant"}
wild_animals = {"lion","tiger","elephant"}
animals = domestic_animals.union(wild_animals)
print(animals)
animals = wild_animals.union(domestic_animals)
print(animals)
animals = wild_animals | domestic_animals
print(animals)
animals = wild_animals.intersection(domestic_animals)
print(animals)