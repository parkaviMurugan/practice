n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
l.reverse()
new=''
for i in l:
  new+=str(i)
print(new)
