a = input("Enter first string: ")
b = input("Enter second string: ")
common = set(a) & set(b)
print("Common letters:", common)