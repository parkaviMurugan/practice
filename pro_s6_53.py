x=input()
f=0
alpha="abcdefghijklmnopqrstuvwxyz"
for i in alpha:
  if i  not in x.lower():
    f=1
if f==1:
  print("no")
else:
  print("yes")
