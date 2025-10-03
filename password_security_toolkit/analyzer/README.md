This is a password strength analyser written in Python. The program takes a password input from the user and gives back a rating (WEAK/MODERATE/STRONG/VERY STRONG).

Breadown of the theory and formula used:

Usually, to calculate the entropy of passwords, the following formulae are used:

(1) Simple Entropy

![Formula](https://latex.codecogs.com/svg.image?H=L.log_2N&colour=333333)

L = length of password, 

N = character set size

This formula is a theoretical formula that assumes maximum randomness and does not punish repetition.

(2) Multinomial Entropy

![Formula](https://latex.codecogs.com/svg.image?&space;H=log_2((L!*26^u*26^l*10^d*32*s)/(u!l!d!s!))&colour=333333)

L = length of password,

u = number of uppercase letters,

d = number of digits,

s = number of symbols

This formula is also a theoretical formula, but it takes into consideration the exact number of individual element types from their respective sets. So, while it rewards character diversity, it still doesn't punish repetition. 

(3) Realized Entropy

![Formula](https://latex.codecogs.com/svg.image?H=-\sum_{i}p_ilog_2(p_i)=-L*(p_i.log_2(p_i))&colour=333333)

L = length of password,

p_i = probability of finding an element from the set of unique characters in the password

Unlike the above two, this isn't a theoretical formula, but, as its name suggests, a "realized" one, which takes into consideration only the unique elements used in the password itself. While it punishes repetition, it does not give a very high entropy value for strong passwords, thus underestimating its security because an attacker would not know the exact distribution/ characters used in advance.


Since the above 3 formulae have some or the other limitations, I created and employed a formula of my own using basic combinatorics that I learnt in 11th grade, in order to reduce the limitations. That formula, is:

![Formula](https://latex.codecogs.com/svg.image?&space;H=log_2(((_{uc}^{26}\textrm{C})*(_{lc}^{26}\textrm{C})*(_{d}^{10}\textrm{C})*(_{s}^{32}\textrm{C})*L!)/(r_1!r_2!..r_L!))&colour=333333)

L = length of password,

u = number of unique uppercase letters,

d = number of unique digits,

s = number of unique symbols,

r_n (n belonging to [1, L]) = number of times the corresponding element is repeating

This formula is a theoretical formula that considers the entropy of cracking the password from a set of similar passwords. This not only punishes repetition, but also gives a high value of entropy for strong passwords.

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd password_security_toolkit
cd analyzer
#Run the script
py password.py
```

Example runs:
```bash
Enter a password: AAAAAAAA
Password Strength: WEAK 
```

```bash
Enter a password: P@sSw0rD
Password Strength: STRONG 
```

```bash
Enter a password: UnBr3@k@bl312
Password Strength: VERY STRONG 
```
