arr = input("Write Your Numbers Like 2,3,4,5,6 : ")
data = [x for x in arr.split(",")]
print (data)
data = tuple(data)

print (data)
