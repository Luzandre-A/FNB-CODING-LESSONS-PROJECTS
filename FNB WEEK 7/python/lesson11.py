fruits = ["apple","banana" ,"cherry","date"]

for fruit in fruits:
    if fruit == "cherry":
        break # Exits the loop if cherry is found
    print(fruit)
    
print()


for fruit in fruits:
    if fruit == "cherry":
        continue # Skips cherry and moves to the iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
       pass # Placeholder, no ation is needed for cherry
    print(fruit)
    
    
    
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 4:
        break # Exits loop when the count is reached

