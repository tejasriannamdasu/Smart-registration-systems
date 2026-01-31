id=input("ID: ")
email=input("Email: ")
password=input("Password: ")
referral=input("Referral Code: ")
flag=0
regno=input("registor number:")
if regno[-1].isdigit()  and int(regno[-1])%2 ==0:
    if id[3] == '-' and id[0:3] == 'CSE' and id[-3:].isdigit():
        flag += 1
    # for password
    if len(password) >= 8 and password == password.capitalize():
        if ("0" in password or "1" in password or "2" in password or "3" in password or "4" in password or
                "5" in password or "6" in password or "7" in password or "8" in password or "9" in password):
            flag += 1
else:
    # for password
    if len(password) >= 8 and password == password.capitalize():
        if ("0" in password or "1" in password or "2" in password or "3" in password or "4" in password or
                "5" in password or "6" in password or "7" in password or "8" in password or "9" in password):
            flag += 1
    if id[3] == '-' and id[0:3] == 'CSE' and id[-3:].isdigit():
        flag += 1
#for email
if email.count('@')==1  and email[0]!='@' and email[-4:]=='.edu' and email[-1]!='@':
    flag+=1
#for referral code
if referral[-1] == '@' and referral[:3] == 'REF' and referral[3:-1].isdigit():
    flag+=1
if flag==4:
    print('APPROVED')
else:
    print('REJECTED')


