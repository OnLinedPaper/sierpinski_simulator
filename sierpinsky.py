import numpy as np
import pylab
from random import randint


#bit of a misnomer, but "midpoint" displaces towards the next point 
#at the user's requested strength. a dis of 0.5 results in the normal 
#fractal. higher values result in "tighter" fractals, lower values 
#result in the pattern becoming less distinct.
def midpoint(p1, p2, dis):
  return [ p1[0] * (1-dis) + p2[0] * dis, p1[1] * (1-dis) + p2[1] * dis ]

#-   -   -   -   -   -   -   -   -  -   -   -   -   -   -   -   -   -   -   -

#get user's input
total_pts = int(input("how many points? "))
iterations = int(input("how many iterations? "))
displace = float(input("how hard to displace? "))

all_p = []

x = 0
y = 0

#request a coordinate pair from the user, for each point they want to create.
#see https://www.mathopenref.com/coordpolycalc.html for polygon coords
for i in range(0, total_pts):
  print("\npoint" , i)
  x = float(input("x value "))
  y = float(input("y value "))
  all_p.append([x,y])

#set to current point
curr_p = all_p[0]

for _ in range(iterations):
  
  #decide which point to displace towards
  val = randint(0,total_pts-1)
 
  #displace towards it
  curr_p = midpoint(curr_p, all_p[val], displace)

  #plot it
  pylab.plot(curr_p[0], curr_p[1], 'm.', markersize=2)

#big reveal
pylab.show()
