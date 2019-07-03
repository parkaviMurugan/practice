x,y=input().split(" ")
x=int(x)
y=int(y)
s=min(x,y)
lit=[]
for i in range(1,s):
  if x%i==0 and y%i==0:
    lit.append(i)
print(max(lit))
