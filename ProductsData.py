class Product:
    def __init__(self,prodname,_price,catid):
        self.prodname=prodname
        self._price=_price
        self.__catid=catid

    def showcategoryid(self):
        print(self.__catid)




p=Product("Tea",10,11)
print(p.prodname)#public
print(p._price)# when _ used, its protected, its accessible, but not recommended, protected means inside the class or child class
#print(p.__catid)##__Name mangling,private ---Gives errord
p.showcategoryid()
---------------------------------------------

Create Student class
    public name,
    protected grade,
    private 3 marks & print calculateTotal with average 