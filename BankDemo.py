#Static Method:
# it belongs to class, not to object(cannot call it with the instance )
# doesn't use selef
# It is used as a helper/utility function kept inside class
#Need
#1) Logic related to class but doesnot depend on obect data


class BankUtil:
    def __init__(self,balance):
        self.balance=balance
            

    @staticmethod
    def is_amt_valid(amt):
        return amt>0

    @staticmethod
    def greet():
        print("Hello")

    def Deposit(self,amount):
        BankUtil.greet()
        if BankUtil.is_amt_valid(amount):
            self.balance+=amount
            print(self.balance)
        else:
            print(self.balance)

    


b=BankUtil(10000)
b.Deposit(10000)
