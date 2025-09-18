import itertools as it

lst = ['A', 'B', 'C', 'D']
perms = it.permutations(lst,2)
perms_lst = list(perms)
print(perms_lst)
print(type(perms))
print(perms)