r=input()
r=r.replace('.','')
word =r.split()
l=[]
for i in range(len(word)):
  if(i%2==0):
    s=word[i]
    l.append(s[::-1])
  else:
    l.append(word[i])
k=" ".join(l)
print(k)
