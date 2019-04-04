operator = (input("Enter + to add, - to substract, / to divide, * to multiply pow to raise to a power: "))
num1 = float((input("Enter a number: ")))
num2 = float((input("Enter another number: ")))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
elif operator == "pow":
    print(num1**num2)
else:
    print("Invalid input!")