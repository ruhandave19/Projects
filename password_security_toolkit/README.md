This folder contains 3 inter-related projects related to cryptography. They are:

(1) Password Strength Analyzer: This takes password input from the user and returns a rating (WEAK/ MODERATE/ STRONG/ VERY STRONG) after computing its entropy in the backend. Repetitions are punished and it uses an entropy model that mixes both theoretical and realized entropy.

(2) Password Generator: This generates a strong password of length 30 (using atleast 1 uppercase letter, lowercase letter, digit and symbol). It uses a theoretical model for generation, thus allowing repetitions.

(3) Demo: This is a merger of the above two projects. It takes length input from the user and gives freedom to include/ exclude uppercase letters, lowercase letters, digits and symbols. It then generates a password accordingly using the generator and then uses the analyzer to compute its entropy and give it a rating.

Two different models for entropy have been used in the analyzer as well as the generator because:

(a) it is important to keep a check on repetitions in the user generated passwords so as to discourage the use of passwords like "AAAAAAAA" and "000000" which are commonly used and susceptible to leaks and to encourage the user to use diverse set of characters, thus resulting in more unique passwords.

(b) allowing repetitions in the generator, which randomly chooses the characters that make up the password from a set, exponentially increases its search space, making the password much harder to crack.

The demo is where the theoretically generated password is tested with the more realized analyzer.