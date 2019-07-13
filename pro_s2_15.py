i=int(input())
l=input().split()
l=[int(i) for i in l]
l.sort(reverse=True)
for i in l:
  print(i)
