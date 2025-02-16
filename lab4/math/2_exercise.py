import math
height=float(input("Height: "))
base1, base2=map(float, input("Base1, Base2: ").split())
trapezoidal=(base1+base2)*0.5*height
print(f"Trapezoidal area: {trapezoidal}")