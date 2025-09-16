n = int(input("enter the value of n "))
i = 0
max = -1
min = 890776655
while i < n:
    num = int(input(f'Enter the {n} numebrs '))
    if num >max:
        max = num
    if num <min:
        min = num
    i+=1
print(max,min)
positive_infinity = float('inf')
negative_infinity = float('-inf')
print(positive_infinity,negative_infinity)