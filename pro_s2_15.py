inp=int(input())
li=input().split()
li=[int(i) for i in li]
li.sort(reverse=True)
k=[]
f=[]
for i in li:
  s=str(bin(i))
  k.append(s.count('1'))
for i in range(len(k)):
  m=max(k)
  p=k.index(m)
  f.append(l[p])
  k[p]=0
for i in f:
  print(i)
