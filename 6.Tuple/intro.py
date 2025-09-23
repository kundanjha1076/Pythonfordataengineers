t1 = (1, 2, 3, 4, 5, 6)
# same as list but immutable
t2 = tuple(t1)
t3 = (3, )
print(type(t3))
for i in t1:
    print(i,end='')