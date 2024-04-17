import time

#defining the function to get the display of orders being prepared and dispatched
def get_order(food_list):
    restaurant_orders=[]
    #storing the placed orders into the central order list of the restaurant by stack based method : extend
    restaurant_orders.extend(food_list)
    #displaying the placed orders which are in progress
    for i in range(0,len(restaurant_orders)):
        print("Preparing Your Order -",restaurant_orders[i])
    #displaying the dispatched orders
    print("\nThe following orders have been dispatched.")
    for _ in range(0,len(restaurant_orders)):
        #for a hypothetical situation the time of preparation of food order is considered to be 5 seconds
        time.sleep(5)       
        print(restaurant_orders[0])
        #emptying the restaurant list when the orders are dispatched: reversing the list, then poping out the last element and then again reversing the list
        #pop and reverse are some other stack based methods used in the function.
        restaurant_orders.reverse()   
        restaurant_orders.pop()
        restaurant_orders.reverse()

# taking input for food orders from the user
number=int(input("Hello! please enter the number of food items to be ordered : "))
orders=[]
for k in range(0,number):
    orders.append(input())

# calling the functions, feeding the orders placed by user into restaurant's list through function to display output
get_order(orders)

