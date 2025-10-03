This project generates a strong password of length 30. Repetitions are allowed to increase the maximum possible searchspace but with a condition, that being atleast 1 uppercase letter, lowercase letter, digit and symbol should be present so as to comply with rules for setting passwords on most apps and websites.

A subfolder, titled 'tests', includes 2 different files, which were used to find out the time difference the system takes in generating a 20 length and 30 length passwords of the same type. Upon running, it was found that there is hardly a difference (~0.0001s, with sometimes the 30 length password taking lesser time to generate), and hence, length 30 was finalized for the project to exponentially increase the search space.

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd password_security_toolkit
cd generator
#Run the script
py generator.py
```

Example run:
```bash
Would you like to generate a password? (y/n) y
Password: `=>(%Vr6r`7`!@HDlu:yxp_=Y;m5mR
Would you like to generate another password? (y/n) n
Thank you
```