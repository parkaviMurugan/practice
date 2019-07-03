x,y=input().split(" ")
x=int(x)
y=int(y)
s=min(x,y)
li=[]
for i in range(1,s):
  if x%i==0 and y%i==0:
    li.append(i)
print(max(li))
