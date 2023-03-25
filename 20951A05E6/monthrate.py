import math
def monthrate(h,d):
  t=h*8*22
  di=t*d
  r=t-di
  return math.ceil(r)
h=int(input())
d=int(input())
print(monthrate(h,d))
