#student max score finder
max_sc=0
score=input("Input a list of student scores in a test: ").split()
for x in range(len(score)):
    score[x]=int(score[x])
for x in range(len(score)):
  if score[x]>max_sc:
    max_sc=score[x]
  else:
    continue
print("The max score of student is: " + str(max_sc))
