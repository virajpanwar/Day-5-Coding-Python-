sum=0
count=0
student_height=input("Enter a list of student heights: ").split()
for n in student_height:
  count=count+1
print(count)
for n in range(0,count):
  student_height[n]=int(student_height[n])
print(student_height)
for n in range(0,count):
  sum=sum+student_height[n]
print("The sum of the heights is: ",sum)
print("The average height is: ",int(sum/count))
