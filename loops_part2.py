#Loops part2   
#Loops Control Statemnets

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break # Exits the loop if cherry if found
    print(fruit) 
    
print()
for fruit in fruits:
    if fruit == "cherry":
        continue # Skips cherry and moves to the iteration
    print(fruit)      
    

print()
for fruit in fruits:
    if fruit == "cherry":
        pass # Placeholder, no action is needed for cherry
    print(fruit)    
    
    
#Using a while loop to count from 1 to 5    
count = 0
while count < 5:
    print(count)
    count += 1 
    if count == 3:
        break # Exits the loop when the count is reached = 3   