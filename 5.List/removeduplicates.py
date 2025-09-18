L1 = [int(i) for i in input().split(' ')]
l2 =[]

for element in L1:
    if element not in l2:
        l2.append(element)
print(l2)

