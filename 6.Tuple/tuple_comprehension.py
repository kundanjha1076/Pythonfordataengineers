T1 = (*(x for x in range(1,5)),)
print(T1)

T2 =tuple(x for x in range(1,5))
print(T2)

T3 = tuple(x**x for x in range(1,10) if x% 2==0)

print(T3)