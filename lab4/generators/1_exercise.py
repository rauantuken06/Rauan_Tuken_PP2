def generator_of_squares(n):
    res=[]
    for i in range(n):
        s=(i+1)**2
        res.append(s)
    yield res
number=int(input("Enter the number: "))
squares=generator_of_squares(number)
for square in squares:
    print(square)