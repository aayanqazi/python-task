inp = int(input("Enter Number: "))
val ={x: x**2 for x in range(inp+1) if(x != 0) }
print(val)