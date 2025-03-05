def add(a,b):
  return a+b

def substract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b


operation_symbol = {
  "+": add,
  "-": substract,
  "*":multiply,
  "/":divide,
}

def calculator():
  next_calt = True
  numb_1 = int(input("Wha'ts your number =? "))
  while next_calt:
    for symbol in operation_symbol:
      print(symbol)

    pick = input("Pick operation = ")
    numb_2 = int(input("What is your next number =?"))
    p_result = operation_symbol[pick](numb_1,numb_2)
    print(f"{numb_1} {pick} {numb_2} = {p_result}")
    next_calculation = input(f"Type 'y' to continue calculating with {p_result}, or type 'n' to start a new calculation:").lower()
    if next_calculation =='y':
      numb_1 = p_result
    else:
      next_calt = False
      print("\n"*20)
  
  calculator()

calculator()


  
