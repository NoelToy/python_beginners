sample={'key1':25,'key2':55}
print(sample)
print(sample['key1'])

#Built In Functions

cpy=sample.copy();
print("This is the copy of 'Sample Dictionary'")
print(cpy)

print("The value of key one is:",end=' ')
print(cpy.get('key2'))

print("Items in the list are:")
print(cpy.items())
print(type(cpy.items()))

print("Key in the dictinary files:")
print(cpy.keys())

print("Valued in the dictionary:")
print(cpy.values())