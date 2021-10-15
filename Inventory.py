import os

product_list=[]
bin_list=[]
class product:
    counter=2000
    def __init__(self,title,description,upc,costprice,sellingprice,category):
        self.title=title
        self.description=description
        self.upc=upc
        self.sku=product.counter
        product.counter+=1
        self.costprice=costprice
        self.sellingprice=sellingprice
        self.category=category
    def get_title(self):
        return self.title
    def set_title(self,new):
        self.title=new
    def get_sku(self):
        return self.sku
    def get_upc(self):
        return self.upc
    def set_upc(self,newupc):
        self.upc=newupc
    def get_costprice(self):
        return self.costprice
    def get_sellingprice(self):
        return self.sellingprice
    def get_description(self):
        return self.description

class inventory:
    def register_product(self):
        title = input("ENTER THE PROD title:")
        description = input("ENTER THE PROD description:")
        while True:
            upc = input("ENTER THE PROD UPC:")
            if len(upc)>8:
                break
            else:
                print("INVALID INPUT, UPC MUST BE MORE THAN 8 DIGITS")
                print("TRY AGAIN!!")
            if self.check_unique_upc(upc):
                break
            else:
                print("Product with same UPC already registered")
                print("TRY AGAIN!!")

        costprice = input("ENTER THE PROD costprice:")
        sellingprice=input("ENTER THE PROD sellingprice:")
        category = input("ENTER THE PROD category:")
        product1 = product(title, description, upc, costprice, sellingprice, category)
        product_list.append(product1)
        print("PRODUCT ADDED SUCCESSFULLY WITH SKU:", product1.get_sku())
        return product1.get_sku()

    def print_product(self,sku):
        temp=self.find_product_by_sku(sku)
        if temp:
            print("PRODUCT TITLE:",temp.get_title())
            print("PRODUCT SKU:",temp.get_sku())
            print("PRODUCT upc:",temp.get_upc())
            print("PRODUCT COSTPRICE: ",temp.get_costprice())
            print("PRODUCT SELLINGPRICE ",temp.get_sellingprice())
            print("PRODUCT DESCRIPTION ",temp.get_description())
        else:
            print("PRODUCT INVALID SKU")

    def remove_product_by_sku(self,sku):
        flag=False
        for prod in product_list:
            if prod.get_sku()==sku:
                product_list.remove(prod)
                flag=True
        for bin in self.product_lookup_by_sku(sku):
            del bin.get_productdict()[sku]
        return flag
    def product_lookup_by_sku(self,sku):
        temp={}
        bins=[]
        for bin in bin_list:
            if sku in bin.get_productdict():
                if bin.get_productdict()[sku]>0:
                    temp[bin.get_location()]= bin.get_productdict()[sku]
                    bins.append(bin)
        if temp:
            for key,value in temp.items():
                print("LOCATION: ",key," QUANTITY: ",value)
        return bins

    def add_product_to_bin(self,sku,location,qty):
        prod=self.find_product_by_sku(sku)
        bin=self.find_bin_by_location(location)
        if bin:
            if sku not in bin.get_productdict():
                bin.get_productdict()[sku]=qty
            else:
                bin.get_productdict()[sku]+=qty
            return bin

    def remove_product_from_bin(self,sku,location,qty):
        bin=self.find_bin_by_location(location)
        if bin:
            if sku in bin.get_productdict():
                if bin.get_productdict()[sku]>=qty:
                    bin.get_productdict()[sku]-=qty
                else:
                    del bin.get_productdict()[sku]
                return True
        return False
    def find_product_by_sku(self,sku):
        for prod in product_list:
            if prod.get_sku()==sku:
                return prod

    def find_bin_by_location(self,location):
        for bin in bin_list:
            if bin.get_location()==location:
                return bin
        print("LOCATION DOES NOT EXIST")
    def check_unique_upc(self,upc):
        for prod in product_list:
            if prod.get_upc()==upc:
                return False
        return True

    def new_bin(self):
        bin1=bin()
        bin_list.append(bin1)
        print("NEW LOCATION ADDED WITH BIN NUMBER:",bin1.get_location())

    def products_in_bin(self,location):
        bin1=self.find_bin_by_location(location)
        if bin1:
            for key,value in bin1.get_productdict().items():
                print("sku:",key,"quantity:",value)




class bin:
    counter=1001
    def __init__(self):
        self.productdict={}
        self.location=bin.counter
        bin.counter+=1

    def get_location(self):
        return self.location
    def get_productdict(self):
        return self.productdict

product1=product("mobile","iphone",18282121,25000,80000,"elect")
product2=product("laptop","avita",12435674,25000,80000,"elect")
product3=product("charger","android",12445632,25000,80000,"elect")
product_list.append(product1)
product_list.append(product2)
product_list.append(product3)
inventory1=inventory()
#print(inventory1.add_product_to_bin(2001,1992))
#print(bin1.get_productlist()[0].get_title())
while True:
    print("**********************************")
    print("1:REGISTER PRODUCT TO STORE")
    print("2:PRODUCT LOOKUP")
    print("3:REMOVE PRODUCT FROM STORE")
    print("4:ADD PRODUCT TO BIN")
    print("5:REMOVE PRODUCT FROM BIN")
    print("6:VIEW PRODUCTs by Location")
    print("7:ADD NEW LOCATION")
    print("**********************************")
    print("----------------------------------")

    temp=int(input("SELECT AN OPTION:"))
    if temp==1:
        inventory1.register_product()
    elif temp==6:
        location=int(input("PLEASE ENTER Location"))
        inventory1.products_in_bin(location)
    elif temp==3:
        print("WARNING!! Deleteing a product will remove it from all Bins")
        if "Y"==input("DO you want to Proceed ? Y/N"):
            sku = int(input("PLEASE ENTER SKU"))
            if inventory1.remove_product_by_sku(sku):
                print("Product with SKU ",sku," Removed sucessfully.")
            else:
                print("Product does not exist")
    elif temp==4:
        sku = int(input("PLEASE ENTER SKU"))
        qty= int(input("PLEASE ENTER QUANTITY"))
        LOCATION = int(input("PLEASE ENTER LOCATION"))
        if inventory1.find_product_by_sku(sku):
            inventory1.add_product_to_bin(sku,LOCATION,qty)
            print("Product added to location ",LOCATION)
        else:
            print("Product does not exist")

    elif temp==5:
        sku = int(input("PLEASE ENTER SKU"))
        qty= int(input("PLEASE ENTER QUANTITY"))
        LOCATION = int(input("PLEASE ENTER LOCATION"))
        if inventory1.find_product_by_sku(sku):
            if inventory1.remove_product_from_bin(sku,LOCATION,qty):
                print("PRODUCT REMOVED")
            else:
                print("PRODUCT WITH SKU:",sku,"DOES NOT EXIST IN LOCATION:",LOCATION)
        else:
            print("Product does not exist")

    elif temp==2:
        sku = int(input("PLEASE ENTER SKU"))
        if inventory1.find_product_by_sku(sku):
            inventory1.print_product(sku)
            inventory1.product_lookup_by_sku(sku)
        else:
            print("Product does not exist")

    elif temp==7:
        inventory1.new_bin()
    else:
        break;
    print("----------------------------------")

    if "N" == input("Do you want to Continue ? Y/N"):
        break;

