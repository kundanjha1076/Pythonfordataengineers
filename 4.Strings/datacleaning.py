stringread = 'These+notes#reveal9Newtonseeking-out an(!underlying structure to/the\\pyramid:the unit of measurement?used>by its builders'
newStr =""
for x in stringread:
    if x.isalpha() or x.isspace():
        newStr+=x
    else:
        newStr+=' '
print(newStr)