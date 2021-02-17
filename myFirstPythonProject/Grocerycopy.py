class Mobile:
    def __init__(self,id,brand,os,price):
        self.id=id
        self.brand=brand
        self.os=os
        self.price=price
    
class MobileStore:
    
    def __init__(self,mobileDbDict,storeName):
        self.mobileDbDict=mobileDbDict
        self.storeName=storeName
    
    def getTotalPriceForGivenBrand(self,brand):
        totalPrice=0
        for i,j in self.mobileDbDict.item():
            if j.brand==brand:
                totalPrice+=j.price
                if j.os.lower()=='ios':
                    totalPrice+=(0.2*j.price)
                elif j.os.lower()=='android':
                    totalPrice+=(0.1*j.price)
                else:
                    totalPrice+=(0.05*j.price)
        return totalPrice
        
    #def getMobileByOsName:
        
if __name__=='__main__':
    
    n=int(input())
    dict={}
    count=0
    for i in range(n):
        id=int(input())
        brand=str(input())
        os=str(input())
        price=int(input())
        dict[count]=Mobile(id,brand,os,price)
        count=count+1    
    store=MobileStore(dict,"mystore")
    inputbrand=str(input())
     
    print(store.getTotalPriceForGivenBrand(inputbrand)
            