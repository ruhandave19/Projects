This is a simple Fibonacci series printer written in C. This program takes input from the user and prints the fibonacci series till the specified position.

Note: The fibonacci series considered here is 0, 1, 1, 2, 3....

Breakdown of the code:
1) A 'for loop' has been used to ensure speed and efficiency (comapred to recursion), especially if the user enters a large number. 
2) If-else if ladder has been used to handle the base cases (ie, when the user enters 1 or 2).
3) Lastly, the code uses the '\b' escape sequence to delete out a "," that would otherwise be printed after the last element, which could have otherwise looked unpresentable and could also cause some confusion.

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd fibonacci_printer
#Compile the C file
gcc fibonacci.c -o fibonacci
#Run the program
./fibonacci
```

Example run:
```bash
Enter a position: 7
The fibonacci series till position 7 is 0, 1, 1, 2, 3, 5, 8
``` 


