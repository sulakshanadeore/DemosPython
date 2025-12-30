class Payment:
    def pay(self,amount):
        print("Processing payment")


class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using CreditCard")

class UPI(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

class Cash(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Cash")
#f--formatted string literal

# payments=Cash()
# payments.pay(1000)

pObj=[CreditCard(),Cash(),UPI()]
for p in pObj:
    p.pay(1000)


