n=int(input())
l=[]
for i in range(n):
  m=int(input())
  l.append(m)
l.sort(reverse=True)
if l[0]==0:
  print("0")
else:
  new=""
  for i in l:
    new+=str(i)
  print(new,end=" ")
