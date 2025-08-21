class account:
    def __init__(self,acc_number,acc_ifsc,acc_amount):
        self.acc_number=acc_number   # public member
        self._acc_ifsc=acc_ifsc      # protected member
        self.__acc_amount=acc_amount # private member
    def know_account_number(self):
        return self.acc_number       # accessing the public member and try to return it
    def know_account_ifsc(self):
        return self._acc_ifsc        # accessing the protected member and try to return it 
    def know_account_balance(self):
        return self.__acc_amount     # accessing the private member and try to return it 
    def set_amount(self,deposit):           # using the setter to update the acc_amount which is private
        self.__acc_amount+=deposit
        return self.__acc_amount
    def get(self):                   # using the getter to retrive the account detail 
        return self.__acc_amount
acc1=account("123456789","SBI12345",1500)
print(acc1.know_account_number())
print(acc1.know_account_balance())
print(acc1.know_account_ifsc())

print(acc1.set_amount(2000))
print(acc1.get())