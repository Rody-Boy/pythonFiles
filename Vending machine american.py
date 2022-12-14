import time
print ("Welcome to the Python Vending Machine.")

# Asking the user how much money they wish to enter.
number_of_10p = int(input("How many 10 pence coins would you like to insert? "))
while number_of_10p < 0:
    number_of_10p = int(input("Please enter a positive number."))

number_of_20p = int(input("How many 20 pence coins would you like to insert? "))
while number_of_20p < 0:
    number_of_20p = int(input("Please enter a positive number."))

number_of_50p = int(input("How many 50 pence coins would you like to insert? "))
while number_of_50p < 0:
    number_of_50p = int(input("Please enter a positive number."))

number_of_100p = int(input("How many 1 pound coins would you like to insert? "))
while number_of_100p < 0:
    number_of_100p = int(input("Please enter a positive number."))

# Creating a variable to store the total amount of money inserted into the vending machine.
change = round(((number_of_10p * 0.10) + (number_of_20p * 0.20) + (number_of_50p * 0.50) + (number_of_100p * 1.00)),2)

# Informing the user how much they have entered in total.
print ("\nIn total you have entered £", change)
time.sleep(2)
# Creating variables for the 5 products and their respective prices. 
product_1, product_1_price = "Flake", 0.55
product_2, product_2_price = "Wispa", 0.50
product_3, product_3_price = "Crunchie", 0.65
product_4, product_4_price = "Milky Way", 0.35
product_5, product_5_price = "Boost", 0.65

# Creating variables to track the number of each items bought,
flakes_bought = 0
wispas_bought = 0
crunchies_bought = 0
milky_ways_bought = 0
boosts_bought = 0

# Informing the user of the choices available and the prices that of each item.
print ("There are 5 products available to pick from;\n")
time.sleep(2)
print ("Item: {}, Price {} ".format(product_1, product_1_price))
print ("Item: {}, Price {} ".format(product_2, product_2_price))
print ("Item: {}, Price {} ".format(product_3, product_3_price))
print ("Item: {}, Price {} ".format(product_4, product_4_price))
print ("Item: {}, Price {} ".format(product_5, product_5_price))
print ("")

# Asking the user to make a selection.
while change > 0:
    customer_choice = input("What would you like to buy? Type N when you are finished \n")
    if customer_choice == "Flake" or customer_choice == "flake" and change >= product_1_price:
        print ("You have chosen a", product_1, "these cost", product_1_price, "each,")
        change = round((change - product_1_price),2)
        flakes_bought = (flakes_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Wispa" or customer_choice == "wispa" and change >= product_2_price:
        print ("You have chosen a", product_2, "these cost", product_2_price, "each,")
        change = round((change - product_2_price),2)
        wispas_bought = (wispas_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Crunchie" or customer_choice == "crunchie" and change >= product_3_price:
        print ("You have chosen a", product_3, "these cost", product_3_price, "each,")
        change = round((change - product_3_price),2)
        crunchies_bought = (crunchies_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Milky Way" or customer_choice == "milky way" and change >= product_4_price:
        print ("You have chosen a", product_4, "these cost", product_4_price, "each,")
        change = round((change - product_4_price),2)
        milky_ways_bought = (milky_ways_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "Boost" or customer_choice == "boost" and change >= product_5_price:
        print ("You have chosen a", product_5, "these cost", product_5_price, "each,")
        change = round((change - product_5_price),2)
        boosts_bought = (boosts_bought + 1)
        print ("You have this much money remaining: £", change)

    elif customer_choice == "N" or customer_choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", flakes_bought)
        print (product_2, "x", wispas_bought)
        print (product_3, "x", crunchies_bought)
        print (product_4, "x", milky_ways_bought)
        print (product_5, "x", boosts_bought)
        print ("You have £", change, "remaining.")
        break

    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", flakes_bought)
        print (product_2, "x", wispas_bought)
        print (product_3, "x", crunchies_bought)
        print (product_4, "x", milky_ways_bought)
        print (product_5, "x", boosts_bought)
        break

    else:
        print ("There has been an error or you may not have enough credit.")