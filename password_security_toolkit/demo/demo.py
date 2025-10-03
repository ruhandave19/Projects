import string
import secrets
print("Welcome!")
print("Here, you can auto-generate a custom password by deciding the length and types of character to be used")
print("The program will then give a rating to the auto-generated password")
a = 1
while a > 0:
    response_1 = input("Would you like to go ahead? (y/n) ")
    if response_1!="y" and response_1!="n":
        print("You have entered an incorrect key. Please enter either 'y' or 'n'.")
        continue
    elif response_1=="n":
        a = 0
    while a > 0:
        if response_1=="y" or response_2 == "2":
            len = input("Enter length: ")
            if len.isdigit()==False or len==0:
                print("Please enter a non-zero numerical value for length")
                continue
            print("Do you want to use:")
            while a > 0:
                response_u = input("Uppercase letters? (y/n) ")
                if response_u!="y" and response_u!="n":
                    print("You have entered an incorrect key. Please enter either 'y' or 'n'.")
                    continue
                else: 
                    break
            while a > 0:
                response_l = input("Lowercase letters? (y/n) ")
                if response_l!="y" and response_l!="n":
                    print("You have entered an incorrect key. Please enter either 'y' or 'n'.")
                    continue
                else: 
                    break
            while a > 0:
                response_d = input("Digits? (y/n) ")
                if response_d!="y" and response_d!="n":
                    print("You have entered an incorrect key. Please enter either 'y' or 'n'.")
                    continue
                else: 
                    break
            while a > 0:
                response_s = input("Symbols? (y/n) ")
                if response_d!="y" and response_d!="n":
                    print("You have entered an incorrect key. Please enter either 'y' or 'n'.")
                    continue
                else: 
                    break
            alphabet = ""
            conditions = ""
        if response_1=="y" or response_2 == "1" or response_2 == "2":
            s = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
            responses = {string.ascii_uppercase: response_u, string.ascii_lowercase: response_l, string.digits: response_d, string.punctuation: response_s}
            conditions_dict = {"any(c.islower() for c in password)": response_u, "any(c.isupper() for c in password)": response_l, "any(c.isdigit() for c in password)": response_d, "any(c in s for c in password)": response_s}
            for k, v in responses.items():
                if v=="y":
                    alphabet = alphabet + k
            for k, v in conditions_dict.items():
                if v=="y":
                    conditions = conditions + k + " and "
            while True:
                password = ''.join(secrets.choice(alphabet) for i in range(int(len)))
                if (conditions):
                    break
            print(f"Password: {password}")
            all_elements = list()
            d = 0
            u = 0
            l = 0
            s = 0
            for i in password:
                all_elements.append(i)
                if i.isdigit():
                    d+=1
                elif i.isupper():
                    u+=1
                elif i.islower():
                    l+=1
                else:
                    s+=1
            element_count = {}
            for x in all_elements:
                if x in element_count:
                    element_count[x]+=1
                else:
                    element_count[x]=1 
            import math
            repetition = 1
            for k, v in element_count.items():
                repetition = repetition * math.factorial(v)
                if v>1:
                    if k.isdigit():
                        d=d-(v-1)
                    elif k.isupper():
                        u=u-(v-1)
                    elif k.islower():
                        l=l-(v-1)
                    else:
                        s=s-(v-1)
            entropy_naive = ((math.comb(10, d))*(math.comb(26, u))*(math.comb(26, l))*(math.comb(32, s))*(math.factorial(int(len))))/repetition 
            entropy = math.log2(entropy_naive)
            print(f"Entropy of the generated password is {entropy:.4f}bits")
            if entropy<28:
                print("Password Strength: WEAK")
            elif 28<=entropy<38:
                print("Password Strength: MODERATE")
            elif 38<=entropy<59:
                print("Password Strength: STRONG")
            else:
                print("Password Strength: VERY STRONG")
            while a>0:
                response_2 = input("To generate another password of the same type, enter 1\nTo generate a different kind of password, enter 2\nTo quit, enter 9\n")
                if response_2!="1" and response_2!="2" and response_2!="9":
                    print("You have entered an incorrect key. Please try again.")
                    continue
                elif response_2=="9": 
                    a = 0
                else:
                    response_1="n"
                    break
print("Thank you")