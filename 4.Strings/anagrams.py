s1 = 'snooze alarms'
s2 = "alas, no more Z's"
s1 = s1.lower()
s2= s2.lower()

for i in s1:
    if i.isalpha():
        if s1.count(i)!=s2.count(i):
            print('Non anagram')
            break
else:
    print('Anagram')