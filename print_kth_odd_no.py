x,y=input().split(" ")
x=int(x)
y=int(y)
l=[]
for i in range(x):
  l.append(int(input()))
r=[]
for i in l:
  if i%2!=0:
    r.append(i)
print(r[y])
