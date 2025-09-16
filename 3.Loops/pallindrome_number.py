input_number = int(input("Enter a number "))
reversed_num=0
original_number = input_number
while input_number > 0:
    rem = input_number % 10
    reversed_num =reversed_num*10+rem
    input_number//=10
if(reversed_num == original_number):
    print("pallindrome number ")
else:
    print("Non Pallindrome number")