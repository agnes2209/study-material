numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)
print("After appending:", numbers)

numbers.extend([70, 80])
print("After extending", numbers)

numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

numbers.remove(40)
print("After removeing 40:", numbers)

last_item = numbers.pop()
print("After pop():", numbers, "| Popped item:", last_item)

print("Index of 30:", numbers.index(30))

print("Count of 20:", numbers.count(20))

numbers.reverse()
print("After reverse():", numbers)

numbers.sort()
print("After sort():", numbers)

numbers.clear()
print("After clear():", numbers)



