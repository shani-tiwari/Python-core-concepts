# encapsulation --- wrapping data and methods in a single unit 

# ways - 
# 1. public    ---  normal 
# 2. protected ---  _variable-name, _method-name 
# 3. private   ---  __variable-name, __method-name 

class Bank : 
    def __init__(self, name, balance) : 
        self.name = name 
        self.__balance = balance 
    def deposit(self, amount) : 
        self.__balance += amount 
        print("Balance : ", self.__balance) 
    def withdraw(self, amount) : 
        if amount > self.__balance : 
            print("Insufficient balance") 
        else : 
            self.__balance -= amount 
            print("Balance : ", self.__balance) 
    def get_balance(self) : 
        return self.__balance 

call = Bank("shani", 1000) 
call.deposit(100) 
call.withdraw(100) 
print(call.get_balance())   