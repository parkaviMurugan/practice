x,y=input().split()
xl=len(x)
yl=len(y)
m=abs(xl-yl)
if xl<=yl:
  s=x
  l=y
else:
  s=y
  l=x
if len(s)==1:
  print(m)
else:
  for i in range(len(s)):
    if s[i]!=l[i]:
      m+=1
  print(m)
