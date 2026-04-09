#  code reusability , organise code , easy to maintain

## single inheritance
# parent class
class papa() :
    def hello() : 
        print("papa")
# child class
class beta(papa) : 
    pass

beta.hello()        # output : papa



# multiple inheritance
class A : 
    def hello() : 
        print("A")

class B : 
    def hello() : 
        print("B")

# method resolution order (mro) - which class inherited first, that class method will be called, same with constructor function
class C(A, B) : 
    pass

C.hello()           # output : A

class C(B, A) : 
    pass
 
C.hello()           # output : B


#  constructor in inheritance 

class A : 
    def __init__(self, name) : 
        self.name = name
    def show(self) :
         print("name : ", self.name)

class B(A) : 
    pass 

call = B("shani")
call.show()           # output : shani

# another
class Animal : 
    def __init__(self, name) : 
        self.name = name
    def show(self) :
         print("Animal name : ", self.name)

class Dog(Animal) : 
    def __init__(self, name, age)  : 
        super().__init__(name)
        self.age = age
    def show(self) :  # method overriding (same name method in child class)
        super().show()
        print("Dog age : ", self.age)

call = Dog("jerman shepherd", 2)
call.show()           # output : jerman shepherd



# multilevel inheritance 
class factory() : 
    def __init__(self, material, zips) : 
        self.material = material 
        self.zips = zips 

class BhopalFactory(factory) : 
    def __init__(self, material, zips, color ) : 
        super().__init__(material, zips)
        self.color = color 

class puneFactory(BhopalFactory) : 
    def __init__(self, material, zips, color, pockets) : 
        super().__init__(material, zips, color)
        self.pockets = pockets 
    def show(self) : 
        print(f"material : {self.material}, zips : {self.zips}, color : {self.color}, pockets : {self.pockets}") 

product = puneFactory("polyester", "ykk", "black", 4)
product.show()
