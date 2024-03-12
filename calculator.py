#Task 1 - Create a Calculator 

num1 = float(input("Please enter the first number: "))

num2 = float(input("Please enter the second number: "))

print("\nCalculator Menu \n1. Add       +\n2. Subtract  -\n3. Multiply  *\n4. Divide    /\n5. Square    **\n")

operator = print(input("Enter the operation you'd like to perform: "))

if operator in ("1" or "+" or "plus" or "add"):
    print(f"The result of {num1} + {num2} = ", num1 + num2)

elif operator in ("2" or "-" or "minus" or "subtract"):
    print(f"The result of {num1} - {num2} = ", num1 - num2)

elif operator in ("3" or "*" or "x" or "times"):
    print(f"The result of {num1} * {num2} = ", num1 * num2)

elif operator in ("4" or "/" or "divide"):
    print(f"The result of {num1} / {num2} = ", num1 / num2)

elif operator in ("5" or "**" or "^2" or "square"):
    print(f"The result of {num1} ** {num2} = ", num1 ** num2)

else:
    print ("Invalid operator. Please enter the figures again.")


