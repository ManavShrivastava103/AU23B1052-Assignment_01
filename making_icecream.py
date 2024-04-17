#Calling the functions created before
from ice_cream import*

#Asking for choice of user
choice = input('Welcome to our desert parlour ONE3!\nWhat would you like to have first "icecream" or "shake" ?\nEnter your choice : ')

#Taking inputs and calling the functions
if choice=='icecream':
    input_scoopsize = input("Enter the size of scoop you want : ")
    number_of_topings = int(input("Enter the number of topings to be added to your scoop (maximum can be 4) : "))
    #displaying different values in arbitary argument for topings in icecream
    #there can be multiple arguments given but the limit is 4 for the scope of particular code
    if number_of_topings==0:
        add_topping(input_scoopsize)
    elif number_of_topings==1:
        top1 = input("Enter the toping:")
        add_topping(input_scoopsize,top1)
    elif number_of_topings==2:
        top1 = input("Enter the toping:")
        top2 = input("Enter the toping:")
        add_topping(input_scoopsize,top1,top2)
    elif number_of_topings==3:
        top1 = input("Enter the toping:")
        top2 = input("Enter the toping:")
        top3 = input("Enter the toping:")
        add_topping(input_scoopsize,top1,top2,top3)
    elif number_of_topings==4:
        top1 = input("Enter the toping:")
        top2 = input("Enter the toping:")
        top3 = input("Enter the toping:")
        top4 = input("Enter the toping:")
        add_topping(input_scoopsize,top1,top2,top3,top4)
    else:
        print("Sorry! You cannot have so many topings together.")

#Taking input for type of shake and calling the function
elif choice=='shake':
    input_shake = input("Enter the flavour of shake you would like to have(fruits or nuts) : ")
    make_shake(input_shake)

else:
    print("Sorry! We are unable to detect or serve your choice at the moment.")


        