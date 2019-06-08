n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
l.sort(reverse=True)
new=""
for i in l:
  new+=str(i)
print(new,end=" ")
