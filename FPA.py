def fpa():

    print("Enter the value of Input: ")
    i_p = int(input())
    print("Enter the value of File: ")
    file = int(input())
    print("Enter the value of Interface: ")
    interface = int(input())
    print("Enter the value of Query: ")
    query = int(input())
    print("Enter the value of Output: ")
    o_p = int(input())
    inputs = [i_p, file, interface, query, o_p]
    print("Enter the type ratio for Input: ")
    r1 = input()
    print("Enter the type ratio for File: ")
    r2 = input()
    print("Enter the type ratio for Interface: ")
    r3 = input()
    print("Enter the type ratio for Query: ")
    r4 = input()
    print("Enter the type ratio for Output: ")
    r5 = input()
   # print(r1, r2, r3, r4, r5)
    print("Enter the value of W1:")
    w1=input()
    print("Enter the value of W2:")
    w2=input()
    print("Enter the value of W3:")
    w3=input()
    wi=list(map(float,(w1,w2,w3)))
    if r1[0].isalpha():
        if r1 == "average":
            l1 = [0, 1, 0]
        elif r1 == "simple":
            l1 = [1, 0, 0]
        elif r1 == "complex":
            l1 = [0, 0, 1]

    elif r1[0].isdigit():
        a, b, c = map(int, r1.split(":"))
        l1 = [a / (a + b + c), b / (a + b + c), c / (a + b + c)]
    #print(l1)
    if r2[0].isalpha():
        if r2 == "average":
            l2 = [0, 1, 0]
        elif r2 == "simple":
            l2 = [1, 0, 0]
        elif r2 == "complex":
            l2 = [0, 0, 1]

    elif r2[0].isdigit():
        a, b, c = map(int, r2.split(":"))
        l2 = [a / (a + b + c), b / (a + b + c), c / (a + b + c)]
    #print(l2)
    if r3[0].isalpha():
        if r3 == "average":
            l3 = [0, 1, 0]
        elif r3 == "simple":
            l3 = [1, 0, 0]
        elif r3 == "complex":
            l3 = [0, 0, 1]

    elif r3[0].isdigit():
        a, b, c = map(int, r3.split(":"))
        l3 = [a / (a + b + c), b / (a + b + c), c / (a + b + c)]
    #print(l3)
    if r4[0].isalpha():
        if r4 == "average":
            l4 = [0, 1, 0]
        elif r4 == "simple":
            l4 = [1, 0, 0]
        elif r4 == "complex":
            l4 = [0, 0, 1]

    elif r4[0].isdigit():
        a, b, c = map(int, r4.split(":"))
        l4 = [a / (a + b + c), b / (a + b + c), c / (a + b + c)]
    #print(l4)
    if r5[0].isalpha():
        if r5 == "average":
            l5 = [0, 1, 0]
        elif r5 == "simple":
            l5 = [1, 0, 0]
        elif r5 == "complex":
            l5 = [0, 0, 1]

    elif r5[0].isdigit():
        a, b, c = map(int, r5.split(":"))
        l5 = [a / (a + b + c), b / (a + b + c), c / (a + b + c)]
   # print(l5)
    list1 = list(map(float, (l1[0], l2[0], l3[0], l4[0], l5[0])))
    list2 = list(map(float, (l1[1], l2[1], l3[1], l4[1], l5[1])))
    list3 = list(map(float, (l1[2], l2[2], l3[2], l4[2], l5[2])))
    #print(list1, list2, list3)
    #print(inputs)
    simple =[]
    average=[]
    complex=[]
    for i in range(len(list1)):
        simple.append((list1[i]*inputs[i]))
   # print(simple)
    for i in range(len(list2)):
        average.append((list2[i]*inputs[i]))
    #print(average)
    for i in range(len(list3)):
        complex.append((list3[i]*inputs[i]))
   # print(complex)
    fi=list(map(float,(sum(simple),sum(average),sum(complex))))
    UFP=0
    for i in range(len(fi)):
        UFP=UFP+((fi[i]*wi[i]))
    print("Enter the no. of characteristics you want to add:")
    n=int(input())
    print("Name them using 1 whitespace in between: ")
    chars=list(input().split())
    c=[]
    for i in range(n):
      print("Enter the value of "+chars[i]+" :")
      c.append(input())
    ci=[]
    for k in c:
        if '%' in k:
            ci.append(float(k[:-1]) / 100)
        else:
            ci.append(float(k))
    p=sum(ci)
    TDI=p
    VAF=TDI*0.01+0.65
    AFP=UFP*VAF
    print("The value of UFP is: ",round(UFP,3))
    print("Value of TDI is: ",round(TDI,3))
    print("The value of VAF is: ",round(VAF,3))
    print("The value of AFP is: ",round(AFP,3))

fpa()