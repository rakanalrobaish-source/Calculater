A = float(input("whats the first number: "))
B = float(input("whats the second number: "))
Op = input("Which of the following operatives do you wish to use? -. +, /, *: ")
if Op == "-":
    print(A - B)
elif Op == "+":
    print(A + B)
elif Op == "*":
    print(A * B)
elif Op == "/":
    print(A / B)
else:
    print("Invalid Operative")
  
