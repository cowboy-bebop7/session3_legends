import math as m
def monthRate(h,d):
    total=h*22*8
    return (m.ceil(total-(total*0.42)))
h=int(input("Enter hourly rate:"))
d=float(input("Enter discount: "))
print(monthRate(h,d))