password = input("Enter a password: ")
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
entropy_naive = ((math.comb(10, d))*(math.comb(26, u))*(math.comb(26, l))*(math.comb(32, s))*(math.factorial(len(password))))/repetition 
entropy = math.log2(entropy_naive)
if entropy<28:
    print("Password Strength: WEAK")
elif 28<=entropy<38:
    print("Password Strength: MODERATE")
elif 38<=entropy<59:
    print("Password Strength: STRONG")
else:
    print("Password Strength: VERY STRONG")