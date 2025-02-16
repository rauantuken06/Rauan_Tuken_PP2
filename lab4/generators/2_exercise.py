def even_nums(n):
    res=[]
    for i in range(0, n):
        if i%2==0:
            res.append(i)
    return res
num=int(input("Enter the number: "))
evens=even_nums(num)
print(evens)