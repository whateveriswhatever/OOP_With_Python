from Bank_Simulation import BankAccount
from Bank_Simulation import Bank

bidvHashMap = {}

acc1 = BankAccount("Son Bui", "sb1", 11234)

bidvHashMap[acc1._ownerRepresentor] = acc1 

print(bidvHashMap)


BIDV = Bank("BIDV")

BIDV.create_account()
BIDV.create_account()

BIDV.manifest_all_accounts()


