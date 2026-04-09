# abstraction --- showing only essential features and hiding unnecessary details 
# if abstract class used - then u have to implement all methods that defined in that class 

# ways - 
# 1. abstract class 
# 2. interface 

from abc import ABC, abstractmethod 

class Car(ABC) : 
    @abstractmethod 
    def start(self) : 
        pass 
    @abstractmethod 
    def stop(self) : 
        pass 

class Tesla(Car) : 
    def start(self) : 
        print("Tesla started") 
    def stop(self) : 
        print("Tesla stopped") 

class BMW(Car) : 
    def start(self) : 
        print("BMW started") 
    def stop(self) : 
        print("BMW stopped") 

call = Tesla() 
call.start() 
call.stop() 

call = BMW() 
call.start() 
call.stop() 