l1 = [5, 4, 3, 3, 4, 5]
l2 =[]
l4 = l1.reverse()
print(l4)
l2 = list(reversed(l1))
print(l2)
if l1 == l2:
    print("Pallindrome list")
else:
    print("Non pallindrome list")


l3 = l2[::-1]
if l1 == l3:
    print("pallindrome")
else:
    print("non pallindrome")