class account():
    def __init__(self,account_number,ifsc_code,amount=0):
        self.account_number=account_number
        self.ifsc_code=ifsc_code
        self.amount=amount
    def balance(self,*args):   # using the method overloading
        if len(args)==0:
            return self.amount
        else:
            amount=self.amount
            for num in args:
                amount+=num
            return amount

class join_account(account):
    def balance(self,deposit):   # using the method overriding here the balance is also implement in the parent class
        return self.amount+deposit

acc1=account("123456789","SBI123456",1)
print(acc1.balance(2,3,4,5,6,7,8,9))     # trying to send more argument to see it handle or not

acc2=join_account("12345","SBI123456",500)
print(acc2.balance(150))