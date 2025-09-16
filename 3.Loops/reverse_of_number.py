input_number = int(input("Enter a number "))
reversed_num = 0
while input_number >0 :
    rem = input_number % 10
    reversed_num=reversed_num*10+rem
    input_number//=10
print(reversed_num)