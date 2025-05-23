# Define a custom exception
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in the account"):
        self.message = message
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw rs.{amount}. Balance is only rs.{balance}.")
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
except InsufficientFundsError as e:
    print("Transaction failed:", e)






# Age Validation
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(message)

def register_user(age):
    if age < 18:
        raise InvalidAgeError()
    print("Registration successful!")

try:
    register_user(16)
except InvalidAgeError as e:
    print("Error:", e)





# Authentication

class LoginFailedError(Exception):
    def __init__(self, message="Invalid username or password."):
        super().__init__(message)

def login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    if username != correct_username or password != correct_password:
        raise LoginFailedError()
    print("Login successful!")

try:
    login("admin", "wrongpass")
except LoginFailedError as e:
    print("Error:", e)