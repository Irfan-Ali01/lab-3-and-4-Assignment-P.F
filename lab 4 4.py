marks = int(input("Enter your marks: "))
if marks < 40:
  grade = "Fail"
elif marks <= 50:
  grade = "D"
elif marks <= 60:
  grade = "C"
elif marks <= 70:
  grade = "B"
elif marks <= 80:
  grade = "A"
else:
  grade = "A-1"
print("Your grade is", grade)