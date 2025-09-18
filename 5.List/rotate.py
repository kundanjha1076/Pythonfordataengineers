lst = [1, 2, 3, 4, 5, 6]
n = int(input("Enter the number of rotation "))
hlist = lst[0:n]
rotated_list = lst[n:len(lst)]
rotated_list+=hlist
print(rotated_list)