def numbers(n):
    for i in range(n, -1, -1):
        yield i
num=int(input("Enter the number:"))
result=numbers(num)
print(list(result))