x = 5    # int
y = 9.3  # float
z = 3j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 7+5j
y = 8j
z = -5j

print(type(x))
print(type(y))
print(type(z)) # class complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z)) # class complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))


# Exercise 1
x = 5
x = float(x)

# Exercise 2
x = 5.5
x = int(x)

# Exercise 3
x = 5
x = complex(x)