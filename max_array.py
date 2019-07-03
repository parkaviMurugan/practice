x,y=input().split(" ")
x=int(x)
y=int(y)
l=[]
k=[]
for i in range(x):
  l.append(int(input()))
for i in range(y):
  k.append(int(input()))
for i in k:
  l.append(i)
  print(max(l),end=" ")
