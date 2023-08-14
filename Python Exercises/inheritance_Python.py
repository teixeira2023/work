'''class Animal:
    def eat(self):
        print("I can eat")
        
class Dog(Animal):
    def bark(self):
        print("I can bark")
        
class Cat(Animal):
    def get_grumpy(self):
        print("I'm getting grumpy")
        
dog1 = Dog() #refere a classe dog
cat1 = Cat()
dog1.bark() #chama a função bark atribuida a dog1
dog1.eat() #chama a função eat atribuida a dog1
cat1.get_grumpy()'''
### CLASS POLYGON ###
class Polygon():
    def __init__(self,sides): 
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")
        
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        Polygon.display_info(self)

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")
        super().display_info()

t1 = Triangle([5,6,7])
perimeter = t1.get_perimeter()
t1.display_info()
print("The perimeter is",perimeter)


q1 = Quadrilateral([5,5,5,5])
perimeter = q1.get_perimeter()
q1.display_info()
print("The perimeter is",perimeter)