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
                    print("{} sent {}VND successfully to {} !".format(self._ownerRepresentor, amountOfMoney, receiver))                
                
                
            
        

# myAcc = BankAccount("Toru", "ccabcxyz", 69)
# myAcc.encrypt_password()
# myAcc.check_current_status()
# myAcc.check_password()
# print(myAcc.decrypt_password())
# # myAcc.change_password()
# myAcc.check_password()
# print(myAcc.decrypt_password())

# mrA = {
#     "name": "Mr. A",
#     "estate": 10000
# }

# myAcc.send_money_to(mrA, 20000)

# print(mrA["estate"])


class Bank:
    def __init__(self, nameOfBank):
        self._nameOfBank = nameOfBank
        self.user_accounts = {}
    
    
    # {"user_real_name": user_account}
    # user aacount:
    # username, password, bank card ID, 
    def create_account(self):
        user_actual_name = input("Enter your name: ")
        password = input("Enter password: ")
        PIN_code = int(input("Enter random 2 to 5 integer digits to create your own PIN validator: "))
        
        if type(PIN_code) != int:
            print("PIN must be numbers !!!")
        
        userAccount = BankAccount(user_actual_name, password, PIN_code)
        
        # self.user_accounts.append(userAccount)
        self.user_accounts[user_actual_name] = userAccount
        print("An user has just been erected a new account !\n>> {}".format(userAccount))
        # print("Accout lake: {}".format(self.user_accounts))
    
    def erect_account(self, real_name, password, PIN_code):
        PIN_code = int(PIN_code)
        if type(PIN_code) != int:
            print("PIN must be numbers !!!")
        
        userAccount = BankAccount(real_name, password, PIN_code)
        
        # self.user_accounts.append(userAccount)
        self.user_accounts[real_name] = userAccount
        print("An user has just been erected a new account !\n>> {}".format(userAccount))
    
    # def withdraw(self, amountOfMoney):
    def manifest_all_accounts(self):
        # for i in range(0, len(self.user_accounts)):
        #     print(">> {}. {}".format(i, self.user_accounts[i]))
        print(self.user_accounts)

    def look_up_account(self, real_name):
        if real_name not in self.user_accounts:
            print("There is no account under the name : {} !!!".format(real_name))
        else:
            account = self.user_accounts[real_name]
            # print("--> Representor : {}\n--> Password: {}\n--> PIN : {}".format(account))
            account.check_current_status()
    
    def retrieve_account(self, real_name):
        return self.user_accounts[real_name] if real_name in self.user_accounts else None
    
    def validate_account_existence(self, real_name):
        # if real_name not in self.user_accounts:
        #     return False
        # else:
        #     return True
        return False if real_name not in self.user_accounts else True
    
    def validate_none_existence_account_response(self, realname):
        return "{} ain't existed !!!".format(realname)
    
    def sending_money_from_C2C(self, customer1, customer2):
        isCustomer1Existed = self.validate_account_existence(customer1)
        isCustomer2Existed = self.validate_account_existence(customer2)
        
        if not isCustomer1Existed or not isCustomer2Existed:
            print("Cannot unveil customer {}'s account either customer {}'s account !!!".format(customer1, customer2))
        elif not isCustomer1Existed:
            print(self.validate_none_existence_account_response(customer1))
        elif not isCustomer2Existed:
            print(self.validate_none_existence_account_response(customer1))
        else:
            custome1_account = self.retrieve_account(customer1)
            customer2_account = self.retrieve_account(customer2)
            
            amountOfMoney = int(input("Enter the amount of money that customer {} want to send to customer {}: ".format(customer1, customer2)))
            
            customer1.send_money_to(customer2, amountOfMoney)
            print("The transaction has been completed successfully !")
            
        
    
# BIDV = Bank("BIDV")

# BIDV.erect_account("Toru Wick", "asdasdasd", "6996")
# BIDV.erect_account("La Thieu", "asdasdasd", "6926")
# BIDV.erect_account("Son Bui", "asdasdasd", "69121")
# BIDV.erect_account("Lam Nguyen", "asdasdasd", "1123")

# BIDV.manifest_all_accounts()
# BIDV.look_up_account("Son Bui")
# BIDV.look_up_account("Lam Nguyen")

# BIDV.sending_money_from_C2C("Son Bui", "Lam Nguyen")
