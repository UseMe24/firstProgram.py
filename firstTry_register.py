print("You are WELCOME  to our Bar DAYNIGHT.\nPlease Fill The Register.\n")
firstName = input("Enter Your firstName: ")
lastName = input("Enter Your lastName: ")
if not firstName.isalpha() or not lastName.isalpha():
    print("Name must contain only alphabets (A-Z)")
    exit()
mobile = input("Enter mobile number (MUST 9 NUMBERS): ")
if not mobile.isdigit() or not (9 <= len(mobile) <= 11):
    print('WRONG MOBILE NUMBER')
    exit()
if firstName and lastName and mobile:
    print("\n.................\nThanks For Register In Our Bar\n.................\n")
else:
    print("WARNING: You didn't fill the Form")
    exit()
print(f'Please Enter Your Age To Get Your PassID')
age = int(input('Enter Your Age: '))
if age>=18:
    idPass = f"{firstName[0:1]}{lastName[1:2]}{mobile[0:3]}"
else:
    print('Your Age is not enough to enter this Bar. "Be Aware From Drinking Alcohol."')
    exit()
names = firstName.strip().upper()+' '+lastName.strip().upper()
print(f"\nHello Mr.{names}. This is Your PassID:({idPass.upper()}) ... DON'T FORGET.\n..................\nENJOY YOURSELF AND HAVE A DRINK.")

#editedFile
#2nd time

#Using Termux

