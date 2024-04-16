def get_order(food_list):
    for i in range(0,len(food_list)):
        print("Preparing Your Order -",food_list[i])
    print("The following orders have been dispatched.")
    for _ in range(0,len(food_list)):
        print(food_list[0])
        food_list.reverse()
        food_list.pop()
        food_list.reverse() 

number=int(input("Hello! please enter the number of food items to be ordered : "))
orders=[]
for k in range(0,number):
    orders.append(input())

get_order(orders)

