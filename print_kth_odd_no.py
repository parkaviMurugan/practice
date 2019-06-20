x,y=input().split(" ")
x=int(x)
y=int(y)
l=[]
r=[]
for i in range(x):
  l.append(int(input()))
for i in l:
  if i%2!=0:
    r.append(i)
print(r[y-1])
