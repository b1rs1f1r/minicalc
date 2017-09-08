start="""
(1) addition
(2) extraction
(3) multiplication
(4) division
(5) find square
(6) find squareroot
"""

print(start)

while True:
    question=input("Enter the number of process (q for exit): ")

    if question == "q":
        print("Exiting...")
        break

    elif question == "1":
        num1 = int(input("Enter the first number for addition: "))
        num2 = int(input("Enter the second number for addition: "))
        print(num1,"+",num2,"=",num1+num2)


    elif question=="2":
        num3 = int(input("Enter the first number for extraction: "))
        num4 = int(input("Enter the second number for extraction: "))
        print(num3, "-", num4, "=", num3 - num4)


    elif question=="3":
        num5=int(input("Enter the first number for multiplication: "))
        num6=int(input("Enter the second number for multiplication: "))
        print(num5,"x",num6,"=",num5*num6)


    elif question=="4":
        num7=int(input("Enter the first number for division: "))
        num8=int(input("Enter the second number for division: "))
        print(num7,"/",num8,"=",num7/num8)


    elif question=="5":
        num9=int(input("Enter the number for find square: "))
        print(num9, "square =",num9**2)


    elif question=="6":
        num10=int(input("Enter the number for find squareroot: "))
        print(num10,"squareroot =",num10**0.5)


    else:
        print("Wrong Enter!")
        print("Enter a option below: ",start)
