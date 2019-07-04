i,y=input().split()
y=int(y)
l=input().split(" ")
l=[int(x) for x in l]
if y in l:
  print("Yes")
else:
  print("No")
