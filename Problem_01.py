#Defining the function to search for availability of a tshirt brand in shop "One3" :
def get_tshirt(brand_name):
    name_of_user = get_name()
    #Below is the list of brands available in shop, (high in demand brands should be kept first to reduce the searching time)
    one3_shop_itemlist = ["Zara","Van Heusen","Nike","Arrow","Roadster","Allen Solly","Jack & Jones","Levi's","US Polo"," Calvin Klein","Wrogn","H&M"]
    for i in range(0,len(one3_shop_itemlist)):
        if one3_shop_itemlist[i]==brand_name:
            print("Hi",name_of_user,", the brand you are looking for is available in our store ")
            break
    else:
        print("Hi",name_of_user,", Unfortunately the brand you are looking for is not available in our store ")

#Defining the helper function to get the name of user 
def get_name():
    user_name= input("Please enter your username : ") 
    return user_name

#Using the function to get the tshirt brand
print("\nWelcome to our clothing shop ONE3.")
input_by_user = input("Enter the name of the tshirt brand you want : ")
get_tshirt(input_by_user)