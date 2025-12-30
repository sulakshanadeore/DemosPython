class Products:
    def __init__(self):
       pass


    def get_prodid(self):
        return self.__productid
    
    def set_prodid(self,pid):
        self.__productid=pid

    def set_prodname(self,pname):
        self.__productname=pname

    def get_prodname(self):
        return self.__productname


p_obj=Products()
p_obj.set_prodid(1000)
p_obj.set_prodname("Tea")
print(p_obj.get_prodid())
print(p_obj.get_prodname())


