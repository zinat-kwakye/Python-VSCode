#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

#class BankAccount():
 #   def __init__(self, name, accountNumber, balance):
  #      self.name = name
   #     self.accountNumber = accountNumber
    #    self.balance = balance

    #def accountOverview(self):
  #      print("Name:",self.name,"\nAccount Number:",self.accountNumber,"\nBalance: £",self.balance)

 #   def moneyWithdraw(self):
 #       self.balance = float (self.balance - (float(input("Enter amount to withdraw: £"))))
#        print ("Money withdrawn. New balance: £",self.balance)

 #   def moneyDeposit(self):
 #       self.balance = float (self.balance + (float(input("Enter amount to deposit: £"))))
  #      print ("Money deposited. New balance: £",self.balance)

#account1 = BankAccount("Zinat", 594632455, 3334)

#print (account1.accountOverview())     

#print (account1.moneyWithdraw())

#print (account1.moneyDeposit())


#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def carMake(self):
        self.make = input("Input the make of the car:")
        print (self.make)

    def carModel(self):
        self.model = input("Input the model of the car:")
        print (self.model)

    def carYear(self):
        self.year = input("Input the year of the car:")
        print (self.year)

    def carOverview(self):
        print("Car Overview\nMake:",self.make,"\nModel:",self.model,"\Year:",self.year)

car1 = Car("Toyota", "Prius", "2020")

print (car1.carModel())