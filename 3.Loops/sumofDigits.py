input_number = int(input("enter a number "))
sum_of_digits = 0
while input_number > 0:
    rem = input_number %10
    sum_of_digits+=rem
    input_number=input_number//10
print(sum_of_digits)