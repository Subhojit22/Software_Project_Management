print("Enter the number of modules: ")
N=int(input())
print("Is weight same for each module?(Yes/No)")
choice=str(input())
sum=0
if choice=="Yes"or choice=="yes":
    print("Enter the value of weight:")
    w = float(input())
    print("Enter the name of the modules (Each are 1-space separated):")
    name=list(input().split())
    for i in(name):
      print("Enter i/p and o/p value for "+i+" :")
      i_p,o_p=map(int,input().split())
      hk=w*pow(i_p*o_p,2)
      sum=sum+hk
    print("Total value of HK is:",sum)
else:
    print("Enter the name of the modules (Each are 1-space separated):")
    name = list(input().split())
    for i in (name):
        print("Enter i/p and o/p value for " + i + " :")
        i_p, o_p = map(int, input().split())
        print("Enter the weight for "+i+" :")
        w = float(input())
        hk = w * pow(i_p * o_p, 2)
        sum = sum + hk
    print("Total value of HK is:", sum)