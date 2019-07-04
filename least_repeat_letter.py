i=input()
i=i.casefold()
n=''
for x in i:
  if i.count(x)==1:
    n+=" "+x
print(n)
