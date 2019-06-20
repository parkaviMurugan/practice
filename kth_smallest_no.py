x,y=input().split(" ")
x=int(x)
y=int(y)
l=[]
for i in range(x):
  l.append(int(input()))

l.sort(reverse=False)
print(l[y-1])
