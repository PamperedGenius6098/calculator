ch='y'
while ch=='y' or ch=='Y':
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    op=int(input("1.Multiply\n2.Divide\n3.Add\n4.Substract\nEnter the option you want:"))
    if op==1:
        c=a*b
        print(c)
    elif op==2:
        c=a/b
        print(c)
    elif op==3:
        c=a+b
        print(c)
    elif op==4:
        c=a-b
        print(c)
    else:
        print("Wrong input")
    ch=input("Do you want more y/n:")
print("Thanks for testing!")
