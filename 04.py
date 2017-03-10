a = input("Enter Your String With Number: ")
ab = len(a)
letters = 0
digits = 0
for val in range(ab):
    key = a[val]
    if key.isdigit():
        digits = digits + 1
    elif (key.isalpha()):
        letters = letters +1

print ("LETTERS: " , letters)
print ("DIGITS: " , digits)
