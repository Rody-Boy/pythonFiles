def title():
	return ('Vending Machine For Your Favorite Drinks')
	
def end():
	print('Thank you for using my Vending Machine please come again')

print(title())
		
onepesos= int(input("How many 1 peso coins would you like to insert? "))
fivepesos= int(input("How many 5 pesos coins would you like to insert? "))
tenpesos= int(input("How many 10 pesos coins would you like to insert? "))
twentypesos= int(input("How many 20 pesos coins would you like to insert? "))

coins= round(((onepesos* 1) + (fivepesos* 5) + (tenpesos* 10) + (twentypesos * 20)),2)

print ("\nIn total you have entered the money of php", coins)

coke, coke_price='coke', 25
pepsi, pepsi_price='pepsi',30
royal, royal_price='royal',35
rc, rc_price='rc',40

coke_sold=0
pepsi_sold=0
royal_sold=0
rc_sold=0

print('Please Choose What Drinks You Should Buy;\n')
print ("{}, PHP {} ".format(coke, coke_price))
print ("{}, PHP {} ".format(pepsi, pepsi_price))
print ("{}, PHP {} ".format(royal, royal_price))
print ("{}, PHP {} ".format(rc, rc_price))
print ("")

while coins > 0:
    customer_choice = input("What Drink Do you Crave the Most??\n")
    if customer_choice == "coke" and coins >= coke_price:
        print ("You have chosen a drink named", coke, "your bill is", coke_price, "each,")
        coins = round((coins- coke_price),2)
        coke_sold = (coke_sold+ 1)
        print ("Your remaining balance as of this moment is: Php", coins)
        end()
        
        
    elif customer_choice == "pepsi" and coins >= pepsi_price:
        print ("You have chosen a drink named", pepsi, "your bill is", pepsi_price, "each,")
        coins = round((coins- pepsi_price),2)
        pepsi_sold = (pepsi_sold+ 1)
        print ("Your remaining balance as of this moment is: Php", coins)
        end()
       
         
    elif customer_choice == "royal" and coins >= royal_price:
        print ("You have chosen a drink named", royal, "your bill is", royal_price, "each,")
        coins = round((coins- royal_price),2)
        royal_sold = (royal_sold+ 1)
        print ("Your remaining balance as of this moment is: Php", coins)
        end()
        
    elif customer_choice == "rc" and coins >= rc_price:
        print ("You have chosen a drink named", rc, "your bill is", rc_price, "each,")
        coins = round((coins- rc_price),2)
        rc_sold = (rc_sold+ 1)
        print ("Your remaining balance as of this moment is: Php", coins)
        end()
        
      
        
