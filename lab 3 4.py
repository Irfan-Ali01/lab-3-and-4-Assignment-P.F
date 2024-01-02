num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def is_positive(num):
  return num > 0
def is_negative(num):
  return num < 0
def is_even(num):
  return num % 2 == 0
def is_odd(num):
  return num % 2 != 0
def is_multiple_of_3(num):
  return num % 3 == 0
print("Both numbers are positive:", is_positive(num1) and is_positive(num2))
print("At least one of the numbers is positive:", is_positive(num1) or is_positive(num2))
print("Both numbers are negative:", is_negative(num1) and is_negative(num2))
print("At least one of the numbers is negative:", is_negative(num1) or is_negative(num2))
print("Both numbers are even:", is_even(num1) and is_even(num2))
print("At least one of the numbers is even:", is_even(num1) or is_even(num2))
print("Both numbers are odd:", is_odd(num1) and is_odd(num2))
print("At least one of the numbers is odd:", is_odd(num1) or is_odd(num2))
print("Both numbers are multiple of 3:", is_multiple_of_3(num1) and is_multiple_of_3(num2))
print("At least one of the numbers is multiple of 3:", is_multiple_of_3(num1) or is_multiple_of_3(num2))