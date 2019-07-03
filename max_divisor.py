x,y=input().split(" ")
x=int(x)
y=int(y)
s=min(x,y)
l=[]
for i in range(1,s):
  if x%i==0 and y%i==0:
    l.append(i)
print(max(l))
