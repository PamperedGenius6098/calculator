ch='y'
while ch=='y' or ch=='Y':
    a=int(input("Enter first no."))
    b=int(input("Enter second no."))
    op=int(input("1.Multiply\n2.divide\n3.add\n4.substract\nEnter the option you want:"))
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
        print("wrong input")
    ch=input("do you want more y/n:")
print("thanks")
