i=input()
l=[]
l.append(i[0])
for x in range(1,len(i)):
  if x%3==0:
    l.append(i[x])
n=''
for i in l:
  n+=i
print(n)
