import string
import secrets
a = 1
while a>0:
    response_1 = input("Would you like to generate a password? (y/n) ")
    if response_1!="y" and response_1!="n":
        print("You have entered an incorrect key. Please either 'y' or 'n'.")
        continue
    else:
        break
if response_1=="n":
    a = 0
while a > 0:
    if response_1=="y" or response_2=="y":
        s = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(30))
            if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in s for c in password)):
                break
        print(f"Password: {password}")
        while a>0:
            response_2 = input("Would you like to generate another password? (y/n) ")
            if response_2!="y" and response_2!="n":
                print("You have entered an incorrect key. Please either 'y' or 'n'.")
                continue
            elif response_2=="n":
                a = 0
            else:
                break
print("Thank you")