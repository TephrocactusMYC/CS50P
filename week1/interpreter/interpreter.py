def main():
    expression=input("Expression: ")
    x, y, z = expression.split(" ")
    if y == "/" and z=="0":
        print("Wrong!")
    else:
        match y:
            case "+":
                print(float(int(x)+int(z)))
            case "-":
                print(float(int(x)-int(z)))
            case "*":
                print(float(int(x)*int(z)))
            case "/":
                print(int(x)/int(z))
main()