input_year = int(input("Enter the year "))
if input_year % 100 == 0:
    if input_year % 400 == 0:
        print("Leap Year")
    else:
        print('Not a leap year')
elif input_year % 4==0:
    print('Leap Year')
else:
    print("Not a leap year ")