def half_adder_sum(a,b):
    return a^b
def half_adder_carry(a,b):
    return a&b
def full_adder_sum(a,b,c):
    return (a^b)^c
def full_adder_carry(a,b,c):
    return ((a^b)&c)|(a&b)
def four_bit_adder(a,b):
    bit_list_1 = []
    bit_list_2 = []
    p = (4-len(bin(a)[2:]))*"0"+bin(a)[2:]
    q = (4-len(bin(b)[2:]))*"0"+bin(b)[2:]
    for i in p:
        bit_list_1.append(int(i))
    for i in q:
        bit_list_2.append(int(i))
    output = ""
    output = str(half_adder_sum(bit_list_1[-1], bit_list_2[-1])) + output
    output = str(full_adder_sum(bit_list_1[-2], bit_list_2[-2], half_adder_carry(bit_list_1[-1], bit_list_2[-1]))) + output
    output = str(full_adder_sum(bit_list_1[-3], bit_list_2[-3], full_adder_carry(bit_list_1[-2], bit_list_2[-2], half_adder_carry(bit_list_1[-1], bit_list_2[-1])))) + output   
    output = str(full_adder_sum(bit_list_1[-4], bit_list_2[-4], full_adder_carry(bit_list_1[-3], bit_list_2[-3], full_adder_carry(bit_list_1[-2], bit_list_2[-2], half_adder_carry(bit_list_1[-1], bit_list_2[-1]))))) + output 
    return output
def twos_complement_representation(a): 
    a_bin = (4-len(bin(a)[3:]))*"0"+bin(a)[3:] 
    a_bin_comp = ""
    for bit in a_bin:
        if bit=="0":
            bit_not = bit.replace("0", "1")
            a_bin_comp = a_bin_comp + bit_not
        else:
            bit_not = bit.replace("1", "0")
            a_bin_comp = a_bin_comp + bit_not
    fba = four_bit_adder(int(a_bin_comp, 2), 1)
    return fba 
def four_bit_adder_subtractor(a,b):
    bit_list_1 = []
    bit_list_2 = []
    if a>=0 and b>=0:
        p = (4-len(bin(a)[2:]))*"0"+bin(a)[2:]
        q = (4-len(bin(b)[2:]))*"0"+bin(b)[2:]
        print(f"A (BINARY): {p}")
        print(f"B (BINARY): {q}")
        print("OPERATION: ADDITION")
    elif a>=0 and b<0:
        p = (4-len(bin(a)[2:]))*"0"+bin(a)[2:]
        q = twos_complement_representation(b)
        print(f"A (BINARY): {p}")
        print(f"B (BINARY): {q} (TWOS COMPLEMENT REPRESENTATION)")
        print("OPERATION: SUBTRACTION")
    elif a<0 and b>=0:
        p = twos_complement_representation(a)
        q = (4-len(bin(b)[2:]))*"0"+bin(b)[2:]
        print(f"A (BINARY): {p} (TWOS COMPLEMENT REPRESENTATION)")
        print(f"B (BINARY): {q}")
        print("OPERATION: SUBTRACTION")
    elif a<0 and b<0:
        p = twos_complement_representation(a)
        q = twos_complement_representation(b)
        print(f"A (BINARY): {p} (TWOS COMPLEMENT REPRESENTATION)")
        print(f"B (BINARY): {q} (TWOS COMPLEMENT REPRESENTATION)")
        print("OPERATION: SUBTRACTION")
    for i in p:
        bit_list_1.append(int(i))
    for i in q:
        bit_list_2.append(int(i))
    output = ""
    output = str(half_adder_sum(bit_list_1[-1], bit_list_2[-1])) + output
    output = str(full_adder_sum(bit_list_1[-2], bit_list_2[-2], half_adder_carry(bit_list_1[-1], bit_list_2[-1]))) + output
    output = str(full_adder_sum(bit_list_1[-3], bit_list_2[-3], full_adder_carry(bit_list_1[-2], bit_list_2[-2], half_adder_carry(bit_list_1[-1], bit_list_2[-1])))) + output   
    output = str(full_adder_sum(bit_list_1[-4], bit_list_2[-4], full_adder_carry(bit_list_1[-3], bit_list_2[-3], full_adder_carry(bit_list_1[-2], bit_list_2[-2], half_adder_carry(bit_list_1[-1], bit_list_2[-1]))))) + output 
    if output[0]=="0":
        print(f"RESULT (BINARY): {output}")
        print(f"RESULT (DECIMAL): {int(output, 2)}")
    elif output=="1000":
        print(f"RESULT (BINARY): {output}")
        print(f"RESULT (DECIMAL): -8")
    else:
        print(f"RESULT (BINARY): {output} (TWOS COMPLEMENT REPRESENTATION)")
        print(f"RESULT (DECIMAL): {-int(twos_complement_representation(int(output, 2))[1:], 2)}")
a = 1
while a>0:
    h = int(input("Enter A (from -8 to 7): "))
    if h<-8 or h>7:
        print("Please enter a number from -8 to 7")
        continue
    else:
        break
if -8<=h<=0:
    ul = 7
    ll = -8-h
    while a>0:
        k = int(input(f"Enter B (from {ll} to {ul}): "))
        if k<-8 or k>7:
            print(f"Please enter a number from {ll} to {ul}: ")
            continue
        else:
            break
else: 
    ul = 7-h
    ll = -8
    while a>0:
        k = int(input(f"Enter B (from {ll} to {ul}): "))
        if k<-8 or k>7:
            print(f"Please enter a number from {ll} to {ul}")
            continue
        else:
            break
{four_bit_adder_subtractor(h,k)}