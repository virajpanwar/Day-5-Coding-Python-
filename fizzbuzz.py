#fizz buzz generator
for x in range(1,101):
  if x%3==0 and x%5==0:
    print("fizzbuzz!")
    continue
  elif x%3==0:
    print("fizz")
    continue
  elif x%5==0:
    print("buzz")
    continue
  else:
    print(x)
