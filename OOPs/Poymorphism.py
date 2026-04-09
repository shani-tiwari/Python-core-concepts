# polymorphism --- many forms 

# method overloading --- python doesn't support 

#  2 ways to implement --- method overriding & duck typing 

class Calculator : 
    def add(self, a, b) : 
        return a + b 
    def add(self, a, b, c) : 
        return a + b + c 
    def add(self, a, b, c, d) : 
        return a + b + c + d 

calc = Calculator() 
print(calc.add(1, 2)) 
print(calc.add(1, 2, 3)) 
print(calc.add(1, 2, 3, 4))         


#  Duck typing 👇🏻👇🏻

class duck :
    def talk(self) : 
        print("quack")
class human :
    def talk(self) : 
        print("hello")

def person(obj) : 
    obj.talk() 

person(duck()) 
person(human()) 