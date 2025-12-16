# response = input("Would you like a food? (Y/N): ")

# if response.upper() == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")

#brocode exercise - python calculator

operator = input("Select the operator to use: (+ - * /): ")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

result = None
result_name = ""

if operator == "+":
    result = num1 + num2
    result_name = "sum"
elif operator == "-":
    result = num1 - num2
    result_name = "difference"
elif operator == "*":
    result = num1 * num2
    result_name = "product"
elif operator == "/":
    if num2 == 0:
        print("Error! Cannot divide to zeros")
    else:
        result = num1 / num2
        result_name = "qoutient"
else:
    print("Invalid operators! Please enter a valid one.")

if result != None:
    print(f"The {result_name} is {result}")