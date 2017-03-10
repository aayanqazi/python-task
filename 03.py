arr = input("Enter Your Number Ex 2,3,4,5,6: ")
are = [x for x in arr.split(",") if int(x) % 2 != 0]

print (",".join(are))
