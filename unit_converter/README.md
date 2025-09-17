This is a simple unit converter written in C. This program takes input from the user and prompts them to enter a unit for conversion corresponding to the input. The user will be continuously asked for a prompt, unless they choose to quit by entering the corresponding key.

The conversions offered are:
1) kms to miles
2) inches to foot
3) cms to inches
4) pounds to kgs
5) inches to metres

Breakdown of the code:
1) A 'for loop' has been used to repeatedly prompt the user for an input.
2) A 'break;' statement is used for when the user enters the corresponding key to exit the conversion loop.
3) An 'if-else if ladder' has been used to guide the compiler to the unit conversion for which the user provided the input.

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/C_projects.git 
#Navigate into the project folder
cd C_projects
#Compile the C file
gcc unit_converter.c -o unit_converter
#Run the program
./unit_converter
```

Example run:
```bash
Following are the options:
1)kms to miles
2)inches to foot
3)cms to inches
4)pounds to kgs
5)inches to metres
To go for conversion, enter the number that the conversion is listed as
To quit, press 9

Enter a value: 4

Enter value in pounds: 100
The entered value in kgs is 45.351

Following are the options:
1)kms to miles
2)inches to foot
3)cms to inches
4)pounds to kgs
5)inches to metres
To go for conversion, enter the number that the conversion is listed as
To quit, press 9

Enter a value: 1

Enter value in kms: 57
The entered value in miles is 35.426

Following are the options:
1)kms to miles
2)inches to foot
3)cms to inches
4)pounds to kgs
5)inches to metres
To go for conversion, enter the number that the conversion is listed as
To quit, press 9

Enter a value: 9

The program has been terminated
```

