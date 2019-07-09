x,y=input().split()
x=int(x)
y=int(y)
f=0
l=input().split()
l=[int(i) for i in l]
for i in range(len(l)):
  for j in range(1,len(l)):
    if l[i]+l[j]==y:
      f=1
      break
if f==1:
  print("yes")
else:
  print("no")
