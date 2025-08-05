operation = input("What Arithemetic Operation would you like to perform?\n" )

if operation.lower() == "add" or operation.lower() == "addition" or operation.lower() == "+":     
       number1 = input("Enter the first number: ")
       number2 = input("Enter the second number: ")
       YourAnswer =int(number1) + int(number2)
       print("YourAnswer is: ", (YourAnswer))

elif operation.lower() == "subtract" or operation.lower() == "subtraction" or operation.lower() == "minus" or operation.lower() == "-":     
       number1 = input("Enter the first number: ")
       number2 = input("Enter the second number: ")
       YourAnswer =int(number1) - int(number2)
       print("YourAnswer is: ", (YourAnswer))

elif operation.lower() == "multiply" or operation.lower() == "multiplicaiton" or operation.lower() == "into" or operation.lower() == "x" or operation.lower() == "*":     
       number1 = input("Enter the first number: ")
       number2 = input("Enter the second number: ")
       YourAnswer =int(number1) * int(number2)
       print("YourAnswer is: ", (YourAnswer))

elif operation.lower() == "divide" or operation.lower() == "division" or operation.lower() == "/":     
       number1 = input("Enter the first number: ")
       number2 = input("Enter the second number: ")
       YourAnswer =int(number1) / int(number2)
       print("YourAnswer is: ", (YourAnswer))


else:
       print("Invalid Operation")




