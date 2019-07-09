x,y=input().split()
x=int(x)
y=int(y)
l=input().split()
l=[int(i) for i in l]
c=0
s=0
while True:
  ma=max(l)
  if s==y:
    c+=1
    break
  elif s<y:
    s+=ma
    c+=1
  elif s>y:
    s-=ma
    l.remove(ma)
    c-=1
print(c-1)
