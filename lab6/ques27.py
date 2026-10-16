a = input("Enter first string: ").lower()
b = input("Enter second string: ").lower()
if len(a) == len(b) and set(a) == set(b):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")