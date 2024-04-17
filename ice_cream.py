#creating a module ice_cream to be used in making icecream
#defining the function for scoop size and topings of an icecream

import webbrowser   #making the code little more alive and interactive
import time

def add_topping(scoop_size,*toppings):      #topings declared as arbitary argument
    print("\nThankyou for placing order!\nYour",scoop_size,"sized ice cream scoop, is getting ready with heavenly topings of your choice :")
    print(*toppings)
    print("Get ready to enjoy!")
    time.sleep(11)
    webbrowser.open("https://media1.tenor.com/images/85bf829a33b31ffae64538b72f77cbb1/tenor.gif?itemid=13495422")


#defining the function for type of shake
def make_shake(choice_of_shake):
    if choice_of_shake=='nuts':
        print("\nThankyou for placing order!\nYour order of Shake-made-with-nuts will be served soon.\nGet ready to enjoy!")
        time.sleep(11)
        webbrowser.open("https://recipes.timesofindia.com/photo/53806799.cms")
    elif choice_of_shake=='fruits':
        print("\nThankyou for placing order!\nYour order of Shake-made-with-fruits will be served soon.\nGet ready to enjoy!")
        time.sleep(11)
        webbrowser.open("https://tse4.mm.bing.net/th?id=OIP.gzYD0tdW2lfBb7KbBISUtgHaE8&pid=Api&P=0&h=180")
    else:
        print("\nSorry! We don't serve this flavour of shake.")    
    