bill_amount = int(input("enter the bill amount "))
if bill_amount >0 and bill_amount <=1000:
    bill_amount=bill_amount-0.1*bill_amount
elif bill_amount >1000 and bill_amount <=5000:
    bill_amount=bill_amount-0.15*bill_amount
elif bill_amount >=10000:
    bill_amount=bill_amount-0.25*bill_amount
else:
    print("enter a valid bill amount") 

print(bill_amount)