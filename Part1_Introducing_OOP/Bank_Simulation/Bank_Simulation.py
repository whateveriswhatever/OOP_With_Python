from cryptography.fernet import Fernet
import random

# message = "hello word"

# key = Fernet.generate_key()

# fernet = Fernet(key)

# encryptedMsg = fernet.encrypt(message.encode())

# print("original message: {}".format(message))
# print("message after being encrypted: {}".format(encryptedMsg))

key = Fernet.generate_key()
fernet = Fernet(key)

class BankAccount:
    
    # key = Fernet.generate_key()
    # fernet = Fernet(key)
    
    def __init__(self, ownerRepresentor, password, PIN):
        self._ownerRepresentor = ownerRepresentor
        self._ID = "".join([str(random.randint(0, 9)) for _ in range(12)])
        self._initialMoney = 50000
        self._password = password
        self.encrypt_password()
        self._PIN = PIN
    
    def check_current_status(self):
        print("{}\n>>Account ID: {}\n>>Available properity: {}VND".format(self._ownerRepresentor.upper(), self._ID, self._initialMoney))
    
    def encrypt_password(self):
        # key = Fernet.generate_key()
        # fernet = Fernet(key)
        
        # encryptedPassword = fernet.encrypt(self._password.encode())
        # self._password = encryptedPassword
        # return encryptedPassword
        
        if not isinstance(self._password, bytes):
            self._password = fernet.encrypt(self._password.encode())
    
    def decrypt_password(self):
        decryptedPassword = fernet.decrypt(self._password).decode()
        # self._password = decryptedPassword
        return decryptedPassword

    def check_password(self):
        validator = int(input("Enter your PIN: "))
        
        if validator != self._PIN:
            print("Invalid PIN !!!")
        else:
            # actual_password = self.decrypt_password()        
            print("Your password: {}".format(self._password))
    
    def validPIN(self):
        validator = int(input("Enter your PIN: "))
        
        if validator != self._PIN:
            print("Invalid PIN !!!")
            return False
        else:
            return True
        
    
    def change_password(self):
        # validator = int(input("Enter your PIN: "))
        
        # if validator != self._PIN:
        #     print("Invalid PIN !!!")
        # else:
        validator = self.validPIN()
        if not validator:
            print("Invalid PIN !!!")
        else:
            currentPassword = input("Enter your current password: ")
            
            if currentPassword != self.decrypt_password():
                print("Your parsed in password doen't match with your current password ")
            else:
                newPassword = input("Enter new password: ")
                ascertainNewPassword = input("Re-enter new password: ")
                
                if newPassword != ascertainNewPassword:
                    print("Please enter the exact password to be validated !!!")
                else:
                    self._password = newPassword
                    self.encrypt_password()
                    print("Changed password successfully !")
    
    def withdraw(self, amount):
        self._initialMoney -= amount
    
    def perceive(self, amount):
        self._initialMoney += amount
    
    
    def is_run_out_of_money(self):
        return self._initialMoney == 0
                
    def send_money_to(self, receiver, amountOfMoney):
        
        isOutOfMoney = self.is_run_out_of_money()
        
        if isOutOfMoney:
            print("You are out of budget to send money to the other !!!")
        else:
            validator = int(input("Enter your PIN: "))
        
            if validator != self._PIN:
                print("Invalid PIN !!!")
            else:
                currentPassword = input("Enter your current password: ")
            
                if currentPassword != self.decrypt_password():
                    print("Your parsed in password doen't match with your current password ")
                else:
                    # {"Mr.A": {estate: 10000VND}}
                
                    self.withdraw(amountOfMoney)
                    receiver["estate"] += amountOfMoney
                    print("{} sent {}VND successfully to {} !".format(self._ownerRepresentor, amountOfMoney, receiver["name"]))                
                
                
            
        

myAcc = BankAccount("Toru", "ccabcxyz", 69)
myAcc.encrypt_password()
myAcc.check_current_status()
myAcc.check_password()
print(myAcc.decrypt_password())
# myAcc.change_password()
myAcc.check_password()
print(myAcc.decrypt_password())

mrA = {
    "name": "Mr. A",
    "estate": 10000
}

myAcc.send_money_to(mrA, 20000)

print(mrA["estate"])


class Bank:
    def __init__(self, nameOfBank):
        self._nameOfBank = nameOfBank
        self.user_accounts = []
    
    
    # {"user_real_name": user_account}
    # user aacount:
    # username, password, bank card ID, 
    def create_account(self):
        user_actual_name = input("Enter your name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        user_account = {
            "user_actual_name": user_actual_name,
            "username": username,
            "password": password
        }
        
        self.user_accounts.append(user_account)
    
    # def withdraw(self, amountOfMoney):
        
