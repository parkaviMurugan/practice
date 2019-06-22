i=input()
l=list(i)
n=""
s=['a','e','i','o','u','A','I','O','U','E']
for i in l:
  if i in s:
    l.remove(i)
r=l[::-1]
for i in r:
  n+=i
print(n)
