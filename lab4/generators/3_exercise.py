def div_3and4(n):
    res=[]
    for i in range(0, n):
        if i%3==0 and i%4==0:
            res.append(i)
    yield res
number=int(input("Enter the number: "))
result=div_3and4(number)
print(result)