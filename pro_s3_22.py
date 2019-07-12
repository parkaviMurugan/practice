i=int(input())
l=input().split()
l=[int(i) for i in l]
s=0
k=0
for i in range(0,len(l),2):
  s+=l[i]
for i in range(1,len(l),2):
  k+=l[i]
print(max(s,k))
