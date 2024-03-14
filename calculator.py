#Task 1 - Create a Calculator 

num1 = float(input("Please enter the first number: "))

num2 = float(input("Please enter the second number: "))

print("\nCalculator Menu \n1. Add       +\n2. Subtract  -\n3. Multiply  *\n4. Divide    /\n5. Square    **\n")

sign = input("Enter the number of the operation you'd like to perform: ")

if sign == "1" or sign == "+" :
    result = num1 + num2
    print(f"The result of {num1} + {num2} = ", result)
   

elif sign == "2" or sign == "-": #or "minus" or "subtract":
    result = num1 - num2
    print(f"The result of {num1} - {num2} = ", result)
        

elif sign == "3" or sign == "*" or sign == "x":
    result = num1 * num2
    print(f"The result of {num1} * {num2} = ", result)
        

elif sign == "4" or sign == "/": #or "divide":
   result = num1 / num2
   print(f"The result of {num1} / {num2} = ", result)
        

elif sign == "5" or sign == "**" or sign == "xx" or sign == "square":
    result = num1 ** num2
    print(f"The result of {num1} ** {num2} = ", result)
        
else:
    print ("Invalid operator. Please enter the figures again.")




