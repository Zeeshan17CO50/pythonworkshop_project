while(1):
    print("\nMENU: \n1.Add\n2.Subtract\n3.Multiplication\n4.Division\n5.Exit")
    c= int(input("Enter your Choice: "))
    if c==5:
        exit()

    a,b=[int(i) for i in input("Enter the numbers:").split(' ')]
    
    if c==1:
        print(a+b)

    elif c==2:
        print(a-b)

    elif c==3:
        print(a*b)

    elif c==4:
        print(a/b)

    else:
        exit()