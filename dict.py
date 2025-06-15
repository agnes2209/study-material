d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(d)

# Add
d['City'] = 'Delhi'
print("After adding City:", d)

# Update
d['Age'] = '20'
print("After updating Age:", d)

# Remove
del d['Country']
print("After removing Country:", d)

# Accessing a value by key
print("Name:", d['Name'])

#pop
d.pop('City')
print("After popping City:", d)

