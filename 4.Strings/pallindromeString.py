s= 'python'
pstring =''
rev = s[-1::-1]
if s == rev:
    print('Pallindrome')
else:
    pstring=s+s[-1::-1]
    print(pstring)