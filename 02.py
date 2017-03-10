#Exercise 2

x = input("Write Your First number: ")
x = int(x)
y = input("Write Your Second number: ")
y = int(y)

mat = []

for value in range(x):
    arr = []
    for values in range(y):
        arr.append(values*value)

    mat.append(arr)
print(mat)
