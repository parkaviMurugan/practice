n=int(input())
l=[]
r=n
for i in range(n):
  l.append(r)
  r+=1
l.reverse()
new=''
for i in l:
  new+=str(i)
print(new,end=" ")
