a = 10
b = 3
x = 5

#Arithmetic Op
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

#Assignment Op
print("\nAssignment Operators:")
print("Initial x:", x)
x += 2
print("x += 2:", x)

x -= 1
print("x -= 1:", x)

x *= 3
print("x *= 3:", x)

x /= 2
print("x /= 2:", x)

x %= 4
print("x %= 4:", x)

x **= 2
print("x **= 2:", x)

x //= 2
print("x //= 2:", x)


#Comparison Op
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


#Logical Op

print("\nLogical Operators:")
print("AND operator:", a > 5 and b < 5)
print("OR operator:", a < 5 or b < 5)     
print("NOT operator:", not a < b) 

print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

print("\nIdentity Operators:")
x = 100
y = 100
print("x is y:", x is y)
y=200
print("x is y:", x is y)  
print("x is not y:", x is not y)  

