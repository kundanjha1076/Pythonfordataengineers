pwd1 = 'Admin1234'
pwd2 = 'Admin1234'

if pwd1 == pwd2:
    print('Password changed')
elif pwd1.casefold() == pwd2.casefold():
    print('Check the cases')
else:
    print('Password should be same')