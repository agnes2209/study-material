numbers = {10, 20, 30, 20, 40, 20}  # appear only single value even if i put repeaded values
print("Original set:", numbers)

numbers.add(50)
print("After adding 50:", numbers)

numbers.update([60, 70])
print("After updating with [60, 70]:", numbers)

numbers.discard(20)
print("After discarding 20:", numbers)

numbers.remove(30)
print("After removing 30:", numbers)

removed = numbers.pop()
print("After pop():", numbers)
print("Popped element:", removed)

set1= {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

