global Annual_Site_Profit
global Improvement_Cost
global Current_Conversion_Rate 
global Improved_Conversion_Rate 
global Expected_Project_Life
global Interest_rate 

def Future_Gain_from_Improvement_Calculator():
    global Annual_Site_Profit
    global Improvement_Cost
    global Current_Conversion_Rate 
    global Improved_Conversion_Rate 
    global Expected_Project_Life
    global Interest_rate 
    Annual_Site_Profit = float(input("Enter the Annual Profit from the site : "))
    Improvement_Cost = float(input("Enter the Cost of Improvements made on the site : "))
    print("Conversion rate = Visitors who purchased / All site visitors ; Based on this enter the following :")	
    Current_Conversion_Rate = float(input("Enter the Current Conversion Rate : "))			
    Improved_Conversion_Rate = float(input("Enter the Improved Conversion Rate  : "))	
    Expected_Project_Life = float(input("Enter the expected life of project or the time for which project will be active(in years) : "))
    Interest_rate = float(input("Enter the rate of interest : "))
    # Calculating the Future gain and returning its value 
    Future_Gain_from_Improvement = ( Annual_Site_Profit * (Improved_Conversion_Rate/Current_Conversion_Rate) - Annual_Site_Profit )* ((((1+Interest_rate)**Expected_Project_Life) - 1 ) / Interest_rate) - (Improvement_Cost * (1+Interest_rate)**Expected_Project_Life) 
    return Future_Gain_from_Improvement

def Total_Gain_from_Improvement_Calculator():
    global Interest_rate 
    global Expected_Project_Life
    choice = input("Enter 'yes' if you already have the value of Future Gain from Improvement else 'no' : ")
    if choice=='yes':
        Future_Gain_from_Improvement = float(input("Enter the value of future gain from improvement : "))
        Expected_Project_Life = float(input("Enter the expected life of project or the time for which project will be active(in years) : "))
        Interest_rate = float(input("Enter the rate of interest : "))
        Total_Gain_from_Improvement = Future_Gain_from_Improvement/((1+Interest_rate)**Expected_Project_Life) 
        return Total_Gain_from_Improvement
    elif choice=='no':
        Future_Gain_from_Improvement = Future_Gain_from_Improvement_Calculator()
        Total_Gain_from_Improvement = Future_Gain_from_Improvement/((1+Interest_rate)**Expected_Project_Life) 
        return Total_Gain_from_Improvement
    else :
        print("Invalid choice")
        return
   


def Annual_Gain_from_Improvement_Calculator():
    global Expected_Project_Life
    choice = input("Enter 'yes' if you already have the value of Total Gain from Improvement else 'no' : ")
    if choice=='yes':
        Total_Gain_from_Improvement = float(input("Enter the value of total gain from improvement : "))
        Expected_Project_Life = float(input("Enter the expected life of project or the time for which project will be active(in years) : "))
        Annual_Gain_from_Improvement = Total_Gain_from_Improvement/Expected_Project_Life
        return Annual_Gain_from_Improvement
    elif choice=='no':
        Total_Gain_from_Improvement = Total_Gain_from_Improvement_Calculator()
        Annual_Gain_from_Improvement = Total_Gain_from_Improvement/Expected_Project_Life
        return Annual_Gain_from_Improvement
    else :
        print("Invalid choice")
        return
    

def Annual_ROI_Calculator():
    choice = input("Enter 'yes' if you already have the value of Annual Gain from Improvement else 'no' : ")
    if choice=='yes':
        Annual_Gain_from_Improvement = float(input("Enter the value of annual gain from improvement : "))
        Improvement_Cost = float(input("Enter the Cost of Improvements made on the site : "))
        Annual_ROI = Annual_Gain_from_Improvement/Improvement_Cost
        return Annual_ROI
    elif choice=='no':
        Annual_Gain_from_Improvement = Annual_Gain_from_Improvement_Calculator()  
        Improvement_Cost = float(input("Enter the Cost of Improvements made on the site : "))      
        Annual_ROI = Annual_Gain_from_Improvement/Improvement_Cost
        return Annual_ROI
    else :
        print("Invalid choice")
        return


def Total_ROI_Calculator():
    choice = input("Enter 'yes' if you already have the value of Total Gain from Improvement else 'no' : ")
    if choice=='yes':
        Total_Gain_from_Improvement = float(input("Enter the value of total gain from improvement : "))
        Improvement_Cost = float(input("Enter the Cost of Improvements made on the site : "))
        Total_ROI = Total_Gain_from_Improvement/Improvement_Cost
        return Total_ROI
    elif choice=='no':
        Total_Gain_from_Improvement = Total_Gain_from_Improvement_Calculator()  
        Improvement_Cost = float(input("Enter the Cost of Improvements made on the site : "))      
        Total_ROI = Total_Gain_from_Improvement/Improvement_Cost
        return Total_ROI
    else :
        print("Invalid choice")
        return
    
