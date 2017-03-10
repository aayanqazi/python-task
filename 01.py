#Exercise 01
answer = []
for value in range(2000,3201):
    if(value%7 == 0 and value%5!=0):
        answer.append(str(value))

oneLine = ",".join(answer)
print (oneLine)
