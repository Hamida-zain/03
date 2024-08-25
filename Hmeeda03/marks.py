marks=int(input("enter the marks"))
grade=""
if (marks>=90):
    grade="A+"
elif (marks>=80):
  grade="A"
elif (marks>=70):
  grade="B"
elif (marks>=60):
  grade="C"
elif (marks>=50):
  grade="D"
elif (marks>=40):
  grade="E"
else :grade="Fail"
print("Marks : ",marks)
print("Grade : ",grade)