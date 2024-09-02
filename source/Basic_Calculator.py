print("We are here to make a calculator\n")

a = float(
    input("Enter the first number: ")
)  #Taking input from user and Typecasting from string to float datatype
b = float(input("Enter the second number: "))

op = input("Enter the operator: ")  #Taking operator as input from user

if op == '+':
    ans = a + b
    print("The addition is: ", ans)
elif op == '-':
    ans = a - b
    print("The difference is: ", ans)
elif op == '*':
    ans = a * b
    print("The multiplication is: ", ans)
elif op == '/':
    ans = a / b
    print("The division is: ", ans)
elif op == '%':  #Modulus operator gives the remainder
    ans = a % b
    print("The modulus is: ", ans)
