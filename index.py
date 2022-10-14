print("\n" * 5)

from dataclasses import dataclass
import datetime                    
import os
from re import A


        
list_foods = []                    
list_drinks = []                   
list_services = []                 

list_item_price = [0] * 100        
                                  
var_discount_1 = 200                      
var_discount_2 = 1000                     
var_discount_3 = 5000                     
var_discount_1_rate = 0.05                
var_discount_2_rate = 0.10                
var_discount_3_rate = 0.15                


navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 


def def_default():
    global list_drinks, list_foods, list_services, list_item_order, list_item_price     
    list_item_order= [0] * 100                    
def_default()

def def_main():
    
    
        print("*" * 28 + "TIFFIN ORDERING SYSTEM" + "*" * 24 + "\n") 
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(D) ORDER DETAILS\n"
              "\t(P) PAYMENT\n"
              "\t(c) CONTACT DIRECTLY\n"
              "\t(E) EXIT\n"+
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'O'):                                          
                print("\n" * 10)                                        
                def_order_menu()                                          
                                                                  
            elif (input_1 == 'D'):                                        
                print("\n" * 10)                                        
                def_order_details()                                              
                                                                   
            elif (input_1 == 'P'):                                        
                print("\n" * 10)                                         
                def_payment()
                
            elif (input_1 == 'C'):                                        
                print("\n" * 10)                                         
                def_contact()
                                                                    
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           
                                                                   
            else:                                                                                 
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     
        else:                                                                                     
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")        

                                                   


def def_option():
    print("-----Please select the given option.----")
    choice = int(input("For registration Type 1 and For logging in Type 2: "))
    if choice == 1:
       regi()
    elif choice == 2:
        login()

def regi():
    ud = open("User_Data.txt", "r")
    username=(input("Craete user name: "))
    password=input("Create a password: ")
    password1=input("confirm password: ") 
    d=[]
    f=[]
    for i in ud:
        a,b = i.split(",")
        b=b.strip()
        c=a,b
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))   

    if password!=password1: 
        print("Password don't match, Please try again: \n")
        regi()
    elif username in d:
            print("***user exits***")
            print("-----Please try again----")
            regi()
    else: 
        ud=open("User_Data.txt", "a")
        ud.write(username+","+password+"\n")
        ud.close()
        print("*****registration successful*****\n")
        login()
 

def login():
    print(" ")
    print("**************enter details to lOGIN***************")
    ud=open("User_Data.txt", "r")
    username=(input("Please enter username: "))
    password=input("Please enter  password: ")

    if not len(username or password)<1 :
        if True:
         d=[]
         f=[]
         for i in ud:
             a,b = i.split(",")
             b=b.strip()
             c=a,b
             d.append(a)
             f.append(b)
             data = dict(zip(d, f))

             try:
                if data[username]:
                    try:
                        if password == data[username]:
                            print("Welcome back "+ username)
                            def_main()
                            
                        else:
                            print("Username or Password incorrect")
                            # break
                    except:
                        print("Password or Username incorrect")
                        # break
                else:
                    print("User not found")
                    # break
             except:
                print("user or password not found")
        else:
            print(" ")
                  # break
    else:
        print("Please enter a value: ")      
        ud.close()      

def def_order_menu():                                                                               
                                                
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(F) FOODS AND DRINKS\n"
              "\t(O) OTHER SERVICES\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'F'):  
                print("\n" * 10)
                def_food_drink_order()
                
            elif (input_1 == 'O'):
                print("\n" * 10)
                def_other_services() 
                
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
           

def def_full_file_reader():                                                                        
    file_foods = open('files'+navigator_symbol+'list_foods.fsd', 'r') 
    for i in file_foods: 
        list_foods.append(str(i.strip())) 
    file_foods.close()

    file_drinks = open('files'+navigator_symbol+'list_drinks.fsd', 'r') 
    for i in file_drinks:
        list_drinks.append(str(i.strip()))
    file_drinks.close()

    file_services = open('files'+navigator_symbol+'list_services.fsd', 'r') 
    for i in file_services:
        list_services.append(str(i.strip()))
    file_services.close()

    i = 0
    while i <= (len(list_foods) - 1): 
        if '$' in list_foods[i]:
            list_foods[i] = str(list_foods[i][:list_foods[i].index('$') - 1]) + ' ' * (20 - (list_foods[i].index('$') - 1)) + str(list_foods[i][list_foods[i].index('$'):])
        i += 1

    i = 0
    while i <= (len(list_drinks) - 1):
        if '$' in list_drinks[i]:
            list_drinks[i] = str(list_drinks[i][:list_drinks[i].index('$') - 1]) + ' ' * (20 - (list_drinks[i].index('$') - 1)) + str(list_drinks[i][list_drinks[i].index('$'):])
        i += 1

    i = 0
    while i <= (len(list_services) - 1):
        if '$' in list_services[i]:
            list_services[i] = str(list_services[i][:list_services[i].index('$') - 1]) + ' ' * (20 - (list_services[i].index('$') - 1)) + str(list_services[i][list_services[i].index('$'):])
        i += 1
def_full_file_reader()

def def_file_sorter(): 
    global list_foods, list_drinks, list_services
    list_foods = sorted(list_foods)
    list_drinks = sorted(list_drinks)
    list_services = sorted(list_services)

    i = 0
    while i < len(list_foods):
        list_item_price[i] = float(list_foods[i][int(list_foods[i].index("$") + 2):]) 
        i += 1

    i = 0
    while i < len(list_drinks):
        list_item_price[40 + i] = float(list_drinks[i][int(list_drinks[i].index("$") + 2):]) 
        i += 1

    i = 0
    while i < len(list_services):
        list_item_price[80 + i] = float(list_services[i][int(list_services[i].index("$") + 2):]) 
        i += 1
def_file_sorter()

def def_food_drink_order():
    while True:
            print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
            print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK + FOOD NAME|        |PRICE|")

            i = 0
            while i < len(list_foods) or i < len(list_drinks):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_foods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  | " 
                else:
                    food = " " * 36 + "| " 
                if i < len(list_drinks):
                    drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                else:
                    drink = ""
                print(food, drink)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Operation: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 10)
                def_payment() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1])) 
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(list_drinks[int(input_1) - 41])) 
                     except:
                        pass

                     input_2 = input("How Many You Want to Order?: ").upper() 
                     if int(input_2) > 0:
                        list_item_order[int(input_1) - 1] += int(input_2) 
                        print("\n" * 10)
                        print("Successfully Ordered!")
                        def_food_drink_order() 
                        break
                     else:
                        print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_other_services():
    while True:
        print("*" * 29 + "OTHER SERVICES" + "*" * 29)
        print(" |NO| |SERVICE NAME|      |PRICE|")  

        i = 0
        while i < len(list_services):
            print(" (" + str(81+ i) + ")" + " " + str(list_services[i])) 

            i += 1

        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

        input_1 = input("Please Select Your Operation: ").upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        if (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        if (input_1 == 'P'):
            print("\n" * 10)
            def_payment() 
            break
        try:
            int(input_1)
            if (int(input_1) > 80) and (int(input_1) < 100):
                print("\n" * 10)
                print("Successfully Ordered: " + str(list_services[int(input_1) - 81])) 
                list_item_order[int(input_1) - 1] = 1
                def_other_services()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        except:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_order_details():
    while True:
        print("*" * 33 + "ORDER DETAILS" + "*" * 33 + "\n")
        file_report = open('files'+navigator_symbol+'report.fsd', 'r').read() 
        print(file_report)
        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        elif (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_payment():
    while True:
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") 
        total_price = 0 

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 
        i = 0
        while i < len(list_item_order): 
            if(list_item_order[i] != 0):
                if (i >= 0) and (i < 40):
                    report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i]) 
                    print(" " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i])) 
                    total_price += list_item_price[i] * list_item_order[i] 
                if (i >= 40) and (i < 80):
                    report_new += "\n" + " " * 17 + str(list_drinks[i - 40]) + "  x  " + str(list_item_order[i])
                    print(" " * 17 + str(list_drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                    total_price += list_item_price[i] * list_item_order[i] 
                if (i >= 80) and (i < 100):
                    report_new += "\n" + " " * 17 + str(list_services[i - 80])
                    print(" " * 17 + str(list_services[i - 80]))
                    total_price += list_item_price[i] * list_item_order[i] 
                i += 1
            else:
                i += 1
        
        if total_price > var_discount_3: 
            total_price -= total_price * var_discount_3_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_3_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_3_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))
        elif total_price > var_discount_2: 
            total_price -= total_price * var_discount_2_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))
        elif total_price > var_discount_1: 
            total_price -= total_price * var_discount_1_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   $ " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))
        else:
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))

        print("\n (P) PAY           (M) MAIN MENU           (D) ORDER DETAILS          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 10)
            print("Successfully Paid!")
            file_report = open('files'+navigator_symbol+'report.fsd', 'a') 
            file_report.write(report_new)
            file_report.close()
            def_default() 
        elif (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        elif (input_1 == 'D'):
            print("\n" * 10)
            def_order_details() 
            break
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
def def_contact():
    print("               ---*call on 183671263*--             \n")
    def_main()

def_option()
