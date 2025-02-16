import math
slides=int(input("The number of slides: "))
lenght=int(input("The lenght: "))
area=(slides*lenght**2)/(4*math.tan(math.pi/slides))
print(f"Regular polygon area: {area}")