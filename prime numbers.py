num = int(input("Enter a number to know if it's a prime number or not: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print (True) 
           
           break  
   else:  
       print (False) 
            
       
num1=int(input("What is the date of your birthday?"))

if num1 not in(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
	print ('Your birthday is a not a prime number')
	
else:
		print('Your birthday is a prime number')
		
