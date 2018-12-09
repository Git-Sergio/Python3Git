while True:
   print("Canculator:")
   print("Please follow the instruction:")
   print("'First choose the arithmetic Operation' press 'Enter'")
   print("'Choose the first number' press 'Enter ")
   print("'Choose the second number' press 'Enter ")
   print("Operation '+' to Add")
   print("Operation '-' to Subtract")
   print("Operation '*' to Multiply")
   print("Operation '/' to Divide")
   print("Operation '%' to Modulo")
   print("Operation '**' to Exponentiate")
   print("Operation '//' to Floor divide")
   print("Operation '00' or press 'ctrl+C' to end the program")

   user_input = input(": ")

   if user_input == "00":
      break

   elif user_input == "+":
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      result = str(num1 + num2)
      print("The answer is " + result)

   elif user_input == "-":
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      result = str(num1 - num2)
      print("The answer is " + result)

   elif user_input == "*":
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      result = str(num1 * num2)
      print("The answer is " + result)

   elif user_input == "/":
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      result = str(num1 / num2)
      print("The answer is " + result)

   elif user_input == "%":
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      result = str(num1 % num2)
      print("The answer is " + result)

   elif user_input == "**":
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      result = str(num1 ** num2)
      print("The answer is " + result)

   elif user_input == "//":
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      result = str(num1 // num2)
      print("The answer is " + result)

   else:
      print("Unknown input")
      
