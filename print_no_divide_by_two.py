def div(x):
  if(x%2!=0):
    print(x)
  else:
    print(x)
    x=x//2
    div(x)
x=int(input())
div(x)
