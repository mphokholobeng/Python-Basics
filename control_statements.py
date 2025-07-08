#Control Statements  

num = 10
if num > 0:
    print("This number is positive")
       
num = 120
if num > 0:
    print("This number is positive") 

num = -15
if num > 0:
    print("This number is positive")
else:
    print("This number is either zero or negative") 
    
 
num = 0       
if num > 0:
    print("This number is positive")
elif num == 0: 
    print("This number is zero")   
else:
    print("This number is either zero or negative") 
    
# Part2 of Control Statements

num1 = int(input("Enter the first number:, "))
num2 = int(input("Enter the second number:, ")) 

if num1 > num2:
    print(num1, "is greater" , num2)
elif num2 > num1: 
    print(num2, "is greater" , num1)   
else:
    print("Both numbers are equal") 
            
