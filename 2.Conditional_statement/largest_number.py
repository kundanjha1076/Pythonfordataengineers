print("Enter three numbers ")
a= int(input())
b= int(input())
c=int(input())
print(a,b,c)

if (a > b) and (a > c) :
    print(" a is largest number ")
elif (b > a) and (b > c):
    print(" b is largest number ")
else:
    print("C is largest number ")