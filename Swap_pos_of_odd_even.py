i=input()
l=list(i)
r=[]
x=''
for s in range(0,len(l)-1,2):
  tmp=l[s]
  l[s]=l[s+1]
  l[s+1]=tmp
for i in l:
  x+=i
print(x)
