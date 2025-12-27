This project trains Support Vector on iris dataset and predicts the species based on user input features.

It was observed that SVC took less time to import and train than Decision Tree (by an order of 10^(-2)seconds), while still giving 100% accuracy. Thus, SVC was finalized for this project.

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd iris_classifier
cd iris_predict
#Install dependencies 
pip install -r requirements.txt
#Run the script
py iris_pred.py
```

Example output:
```bash
Importing and creating train-test split
Done!
Importing and training SVC
Done!
Please input the sepal length in cm (for meaningful result, it should be in the range 4-8cm): 7.3
Please input the sepal width in cm (for meaningful result, it should be in the range 2-4cm): 2.4
Please input the petal length in cm (for meaningful result, it should be in the range 1-7cm): 5.3
Please input the petal width in cm (for meaningful result, it should be in the range 0-2.5cm): 1.8
The predicted species is: virginica
Would you like to get another prediction? (y/n) n
```