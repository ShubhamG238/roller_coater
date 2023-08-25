h=float(input("enter ur height\n"))
if h>120 : # type: ignore
    print("you can ride")
    age=float(input("enter ur age\n"))
    if age<12:
        print("u have to pay $5")
        bill=5
    elif age<18:
        print("u have to pay $7")
        bill=7
    else :
        print("u have to pay $12")
        bill=12
        photo=input("do u want a photo ? y or n\n")
        if photo=='y':
            bill+=3
            print(f'ur total bill is:{bill}')
        else:      
            print(f'ur total bill is {bill}')     
else:
    print('u cant ride')