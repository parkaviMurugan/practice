x,y=input().split()
x=int(x)
y=int(y)
k=[]
l=input().split()
l=[int(i) for i in l]
for i in range(y):
  s=0
  u,v=input().split()
  u=int(u)
  v=int(v)
  for i in range(u-1,v):
    s^=l[i]
  k.append(s)
for i in k:
  print(i)
