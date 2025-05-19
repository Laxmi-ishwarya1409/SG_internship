class BankAccount:
    def __init__(self,acc_number,acc_name,balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = balance

    def deposit_money(self,add_money):
        if add_money > 0:
            self.balance = self.balance+add_money
            print(f"your balance after adding {add_money} is {self.balance}")

        else:
            print("Deposit amount must be positive.")

    def withdraw_money(self,withdraw_money):
        if withdraw_money > self.balance:
            print("Insufficient balance!")
        elif withdraw_money <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= withdraw_money
            print(f"You have withdrawn {withdraw_money} Current balance is {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")



class SavingsAccount(BankAccount):
    def __init__(self, acc_number, acc_name, balance, interest_rate):
        super().__init__(acc_number, acc_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} applied. New balance is {self.balance}")


acc1 = SavingsAccount("12345", "Ish", 1000, 0.05)

acc1.check_balance() 

acc1.deposit_money(500)  

acc1.withdraw_money(200)  

acc1.apply_interest()  

acc1.check_balance()  
