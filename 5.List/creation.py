#ordered collection of hetrogenous elements. 
#mutable
#can have duplicates.



l1 = [1,2,3,4,5]
print(l1)

l2 = list((3,5,7,9))
print(l2)

l3 = list('abcde')
print(l3)

l4 =[]
print(l4)
for item in l1:
    print(item,end=' ')
 
print(l1[2])
l1.remove(5)
print(l1)