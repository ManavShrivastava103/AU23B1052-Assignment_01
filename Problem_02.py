#Providing an additional argument in the function for size, we will provide it some default value to make it optional
def get_tshirt(brand_name,size=None):
    name_of_user = get_name()       #calling the helper function
    #Brand and size lists for tshirts available in the store
    all_brand_list = ["Zara","Van Heusen","Nike","Arrow","Roadster","Allen Solly","Jack & Jones","Levi's","US Polo"," Calvin Klein","Wrogn","H&M"]
    small_size_list=["Zara","Van Heusen","Nike","Arrow","Roadster","Allen Solly"]
    medium_size_list=["Zara","Nike","Allen Solly","Levi's"," Calvin Klein","Wrogn","H&M"]
    large_size_list=["Arrow","Roadster","Allen Solly","Jack & Jones","Levi's","US Polo"]
    extralarge_size_list=["Allen Solly","Jack & Jones","Levi's","US Polo"]
    doublexl_sizelist=["H&M","Allen Solly","Jack & Jones"]
    statement = "in the required size."
    #Selecting the size required
    if size is None:
        search_list=all_brand_list
        statement="."
    elif size=='S':
        search_list=small_size_list
    elif size=='M':
        search_list=medium_size_list
    elif size=='L':
        search_list=large_size_list
    elif size=='XL':
        search_list=extralarge_size_list
    elif size=='2XL':
        search_list=doublexl_sizelist
    else:
        print("Sorry! the required size is not available in our store.")
        return
    #Searching for the brand in particular size list
    for i in range(0,len(search_list)):
        if search_list[i]==brand_name:
            print("Hi",name_of_user,", the brand you are looking for is available in our store",statement)
            break
    else:
        print("Hi",name_of_user,", Unfortunately the brand you are looking for is not available in our store",statement)

#Defining the helper function to get the name of user 
def get_name():
    user_name= input("Please enter your username : ") 
    return user_name

#Using the function to get the tshirt brand along with size filter
print("\nWelcome to our clothing shop ONE3.")
input_brand_name = input("Enter the name of the tshirt brand you want : ")
choice = input("Do you want to filter by size availability? type yes or no : ")
if choice=="yes":
    input_size=input("Enter the size of tshirt required : ")
    get_tshirt(input_brand_name,input_size)
elif choice=='no':
    get_tshirt(input_brand_name)
else:
    print("Invalid choice.")