while True:
    a = float(input("Pehla number: "))
    op = input("Operation (+ - * /): ")
    b = float(input("Dusra number: "))
    if op == "+": print(a+b)
    elif op == "-": print(a-b)
    elif op == "*": print(a*b)
    elif op == "/": print(a/b)
    
    if input("Aur karna hai? (y/n): ") == "n":
        break