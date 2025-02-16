def even_nums(a, b):
    for i in range(a, b+1):
        yield i**2
point1, point2=map(int, input("Enter the two numbers: ").split())
for square in even_nums(point1, point2):
    print(square)