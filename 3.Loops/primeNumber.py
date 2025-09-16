n = int(input())
count =0
for i in range(2,n//2):
    if n%2 ==0:
        print(i)
        count+=1

if count == 0:
    print('Prime Number')
else:
    print('Non Prime Number')
