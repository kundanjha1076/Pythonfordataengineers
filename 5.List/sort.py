l1 = [10, 20, 30, 40, 50, 10, 20, 30]
l1.sort(reverse=True)
print(l1)

l2  = ['coat', 'python', 'black', 'cat']
l2.sort(key=len, reverse=True)
print(l2)

l3 = ['apple', 'Bat', 'cat', 'Dog']
l3.sort()
print(l3)

l4 =[(x.lower()) for x in l3 if len(x)<4] 
print(l4)