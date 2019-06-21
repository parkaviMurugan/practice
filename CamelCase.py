i=input()
l=i.split(" ")
n=""
for i in range(len(l)):
  if(i==len(l)-1):
    n+=l[i].capitalize()
  else:
    n+=l[i].capitalize()
    n+=" "
print(n)
