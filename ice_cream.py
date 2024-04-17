def add_topping(scoop_size,*toppings):
    print("Thankyou for placing order!\nYour",scoop_size,"sized ice cream scoop sprinkled, showered with heavenly topings :",*toppings,"is soon getting ready.\nGet ready to enjoy!")

def make_shake(choice_of_shake):
    if choice_of_shake=='nuts':
        print("Thankyou for placing order!\nYour order of Shake-made-with-nuts will be served soon.\nGet ready to enjoy!")
    if choice_of_shake=='fruits':
        print("Thankyou for placing order!\nYour order of Shake-made-with-fruits will be served soon.\nGet ready to enjoy!")
    else:
        print("Sorry! We don't serve this flavour of shake.")    
    