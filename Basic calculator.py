n = int(input("First number : "))
m = int(input("Second number : "))
z = input("Enter the arithmetic operation : ")
if z == "+":
    print("Addition of", n,"and",m,"is :",n+m)
elif z == "-":
    print("Substraction of", n,"and",m,"is :",n-m)
elif z == "*":
    print("Multiplication of", n,"and",m,"is :",n*m)
elif z == "/":
    print("Division of",n, "and", m, "is :",n/m)
elif z == "**":
    print("Exponential of",n,"and",m,"is :",n**m)
elif z == "//":
    print("Floor division of",n,"and",m,"is",n//m)
elif z == "%":
    print("Modulo of",n,"and",m,"is",n%m)
else:
    print("Sorry can't help with that!")