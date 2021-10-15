# Inventorymanagement
I have build a inventory management system using python programming language.By using this project one can do a lot of things like register a new product to our store,
product lookup,remove product from store,etc.which i will be discussing each one by one.

I have a list known as product_list which will act as database for our project and also a bin_list which conatains the different location where the product is to be storesd.When you will 
execute the program you will be given to choose from 7 options according to your need.so the options and their working is as follows-:

1) REGISTER PRODUCT TO STORE:
   This option will allow the user to register a new product to the store with its unique product code(upc).The user will give the entire information about the product such as its title,
   description,upc,costprice,sellingprice,category.By giving the all the information correctly the product will get registered in our store and product will be assigned a sku number and
   product will be stored in our database product_list also.(exception--> if you will enter a already registered product(upc code) then it will raise a exception that "product with same
   upc is already registered").

2) PRODUCT LOOKUP:
   This option will allow the user to get details of a already registered product in the store.The user will have to give the sku code of the product and the first step of the algorithm
   will find the registered product object from the product_list.If the product is found from the list,then it will print all the details of the product such as its title,upc,description,
   costprice,sellingprice,category.Else if the product is not found from list it will raise exception that "Product does not exist".

3) REMOVE PRODUCT FROM STORE:
   This option will allow the user to remove the product from store.The user will have to give the sku of the product and the algorithm will find the product if it is present in the 
   product_list.If the product is found in the product list the code will delete the product from the product_list.In fact this code will find the same product in all the bins(location)
   and will remove the product from all the bins if found in it.

4) ADD PRODUCT TO BIN:
   This option will allow the user to add product to bin(location).The user will give sku of the product,quantity of the product and location as input.Firstly the code the find if the 
   product with given sku is present in the product_list or not.If it is present the code will now get the product with the given sku and it will find the bin with given location.After
   getting these two values, product and bin, it will add the product and its quantity to the product_dict of the found bin.

5) REMOVE PRODUCT FROM BIN:
   This option will allow the user to remove product from bin(location).The user will give sku of the product,quantity of the product and location as input.Firstly the code will find if the 
   product with given sku and bin is present in product_list and bin_list respectively.Then it will check if the quantity of the product with given sku is greater than the given quantity
   it will remove the quantity from the product_dict of the bin.

6) VIEW PRODUCTs BY LOCATION:
   This option will allow the user to view all the products present in the given location.Firstly the code will find the bin from the bin_list and once we found the bin by the given location
   we will get the product_dict from given bin.The product_dict of the bin will contain of the products.

7) ADD NEW LOCATION
   This option will not expect any input from user.It will simply make an object of the bin class and due to __init__ constructor a new location will be assigned to it.Then the bin object
   will add to the bin_list.
