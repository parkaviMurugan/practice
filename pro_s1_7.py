i=int(input())
s=0
c=0
n=1
while True:
  s=pow(2,n)
  if s==i:
    c=0
    break
  elif(s>i):
    s=pow(2,n-1)
    c=i-s
    break
  n+=1
print(c)
