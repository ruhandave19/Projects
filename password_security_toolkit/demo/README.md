This project allows the user to decide the length of a password, along with whether or not it can have a particular character set (uppercase letters, lowercase letters, symbols and digits). The program then uses the password generator to generate a password, and then uses the analyzer to computer and return the entropy of the password and give it a strength rating. The program also allows looping, by giving the user an option to: Generate another password of the same type (Option 1), generate a new type of password altogether (Option 2) and quit (Option 3). It also deals with wrong type of input entered.

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd password_security_toolkit
cd demo
#Run the script
py demo.py
```

Example run:
```bash
Welcome!
Here, you can auto-generate a custom password by deciding the length and types of character to be used
The program will then give a rating to the auto-generated password
Would you like to go ahead? (y/n) y
Enter length: 8
Do you want to use: 
Uppercase letters? (y/n) n
Lowercase letters? (y/n) n
Digits? (y/n) y
Symbols? (y/n) y
Password: 565;2?<2>
Entropy of the generated password is 32.4822bits
Password Strength: MODERATE
To generate another password of the same type, enter 1
To generate a different kind of password, enter 2
To quit, enter 9
9
Thank you
```