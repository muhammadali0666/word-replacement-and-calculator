def add(a, b):
  result = a + b
  print(str(a) + "+" + str(b) + "=" + str(result))

def sub(a,b):
  result = a - b
  print(str(a) + "-" + str(b) + "=" + str(result))

def mul(a,b):
  result = a * b
  print(str(a) + "*" + str(b) + "=" + str(result))

def div(a,b):
  result = a / b
  print(str(a) + "/" + str(b) + "=" + str(result))

while True:
    
  print("A. Addtion")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")

  choise = input("input your choice: ")

  if choise == "a" or choise == "A":
    print("Addition")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    add(a,b)
  elif choise == "b" or choise == "B":
    print("Subtraction")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    sub(a,b)
  elif choise == "c" or choise == "C":
    print("Multiplication")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    mul(a,b)
  elif choise == "d" or choise == "D":
    print("Division")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    div(a,b)
  elif choise == "e" or choise == "E":
    print("program ended")
    quit()