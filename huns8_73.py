i=input()
x=input()
s=len(i)
t=len(x)
n=""
for j in range(min(s,t)):
  if x[j]==i[j]:
    n+=x[j]
print(n)
