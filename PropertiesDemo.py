class Products:
    def __init__(self,price):
        self._price=price

    @property
    def productid(self):
        return self.__prodid
    

    @productid.setter
    def productid(self,pid):
        if pid>0:
            self.__prodid=pid

    @property       
    def productname(self):
        return self.__prodname


    @productname.setter
    def productname(self,pname):
        if len(pname)>0:
            self.__prodname=pname


    @property       
    def productprice(self):
        return self._price
  

p1=Products(20)
p1.productid=100
p1.prodname="Coffee"
print(f"Productid={p1.productid}")
print(f"Productname= {p1.prodname}")
print(f"Product Price= {p1.productprice}")


p2=Products(30)
p2.productid=101
p2.prodname="Coke"
print(f"Productid={p2.productid}")
print(f"Productname= {p2.prodname}")
print(f"Product Price= {p2.productprice}")