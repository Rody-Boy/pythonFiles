mylist = [1, 3, 7, 13, 17, 23, 27, 31]

evennumber, oddnumber = 0, 0


for num in mylist: 
         
    if num % 2 == 0: 

        evennumber += 1

    else: 

        oddnumber += 1

print(oddnumber)