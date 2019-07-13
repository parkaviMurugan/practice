i=int(input())
l=input().split()
l=[int(i) for i in l]
c=len(l)
for i in range(len(l)-1):
  if l[i]<l[i+1]:
    c+=l[i]
print(c)
