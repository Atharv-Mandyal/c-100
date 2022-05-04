class Bank:
    def __init__(self,nameOfOwner,balance,transaction):
        self.nameOfOwner=nameOfOwner
        self.balance=balance
        self.transaction=transaction
        
    
    def balanceEnquiry(self):
        print("balance is: 23478")
    def lastdeposit(self):
        print("last deposit done on: 4/4/22")
    def lastWithdrawl(self):
        print("last withdrawl done on 2/5/22")
        
   
rahul=Bank("Rahul",23478,"last transaction on 2/5/22(withdrawl)")
print(rahul.balance)
print(rahul.lastWithdrawl())
print(rahul.lastdeposit())
print(rahul.balanceEnquiry())
print(rahul.nameOfOwner)
print(rahul.transaction)