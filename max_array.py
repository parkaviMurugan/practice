x,y=input().split(" ")
x=int(x)
y=int(y)
l=[]
k=[]
r=input()
l=r.split()
l=[int(x) for x in l]
m=input()
k=m.split()
k=[int(x) for x in k]
for i in k:
  l.append(i)
  print(max(l),end=" ")
