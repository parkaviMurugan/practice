x,y=input().split()
f=1
n=''
x=list(x)
y=list(y)
if len(x)<len(y):
  s=x
  l=y
else:
  s=y
  l=x
while True:
  x=n.join(l)
  y=n.join(s)
  if len(s)==0:
    break
  elif y in x:
    f=0
    break
  else:
    s.remove(s[0])
if f==0:
  print("yes")
else:
  print("no")
