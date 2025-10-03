This is a simple unit converter written in C. This program takes input from the user and prompts them to enter a unit for conversion corresponding to the input. The user will be continuously asked for a prompt, unless they choose to quit by entering the corresponding key.

The conversions offered are:
1) kms to miles
2) inches to foot
3) cms to inches
4) pounds to kgs
5) inches to metres

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd unit_converter
#Compile the C file
gcc units.c -o units
#Run the program
./units
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

Enter a value: 9

The program has been terminated
```

