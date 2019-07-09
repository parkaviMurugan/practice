x=int(input())
k=[]
for i in range(x):
  l=input().split()
  l=[int(i) for i in l]
  for i in range(len(l)):
    k.append(l[i])
k.sort()
k=[str(i) for i in k]
n=" ".join(k)
print(n)

