position=int(input())
changement=int(input())
place=[0]*position
for nb in range(position):
   place[nb]=int(input())
for nb in range(changement):
   place1=int(input())
   place2=int(input())
   place[place1], place[place2] = place[place2], place[place1]
for final in range(place):
   print(final)