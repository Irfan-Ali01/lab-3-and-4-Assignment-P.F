A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
C = int(input("Enter the value of C: "))
def add(x, y):
  return x + y
def sub(x, y):
  return x - y
def mul(x, y):
  return x * y
def div(x, y):
  return x / y
print("The value of A + B + C is", add(add(A, B), C))
print("The value of A - B - C is", sub(sub(A, B), C))
print("The value of A * B * C is", mul(mul(A, B), C))
print("The value of A / B / C is", div(div(A, B), C))
print("Is addition associative?", add(A, add(B, C)) == add(add(A, B), C))
print("Is subtraction associative?", sub(A, sub(B, C)) == sub(sub(A, B), C))
print("Is multiplication associative?", mul(A, mul(B, C)) == mul(mul(A, B), C))
print("Is division associative?", div(A, div(B, C)) == div(div(A, B), C))