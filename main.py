print("Welcome to our calculator\n")
print("You will enter 2 numbers and then enter the operation that you want to do")

def add(numOne, numTwo):
  return numOne+numTwo

def subtraction(numOne, numTwo):
  return numOne-numTwo

def multiply(numOne, numTwo):
  return numOne*numTwo

def divide(numOne,numTwo):
  if numTwo == 0:
    print("Sorry you cannot divide by 0")
  return numOne/numTwo

numOne = int(input("Please enter the first number\n"))
numTwo = int(input("Please enter the second number\n"))
operator = str(input("Please enter the operation that you would like to do\n"))

match operator:
  case 'add':
    print("The answer is ", add(numOne, numTwo))
  case '+':
    print("The answer is ", add(numOne, numTwo))
  case 'subtract':
    print("The answer is ", subtraction(numOne, numTwo))
  case '-':
    print("The answer is ", subtraction(numOne, numTwo))