x=int(input("Enter an age:"))
#if-else
if x < 18:
    print("You are a not eligible for voting")
else:
    print("You are eligible for voting")


#ternary operator
print("You are major" if x >= 18 else "You are minor")


#while loop
y=int(input("Enter no of times you want to print Python: "))
while y > 0:
    print("Python")
    y -= 1

# for loop
for i in range(1, 6):
    print(f"Iteration {i}: Python is great!")