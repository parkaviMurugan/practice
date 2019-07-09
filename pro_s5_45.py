i=input()
l=list(i)
l=l[::-1]
for i in l:
  if l[0]=='0':
    l.remove(l[0])
  else:
    break
if l==l[::-1]:
  print("yes")
else:
  print("no")
