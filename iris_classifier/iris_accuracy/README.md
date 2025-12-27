This project demonstrates the accuracy of predicting the iris dataset, with the help of a graph

The iris dataset mainly consists of petal length, petal width, sepal length and sepal width for 3 species of flowers, setosa, versicolor and virginica. We can feed a portion of the dataset for training decision tree and SVM (suport vector machine), and can test their accuracy using the portion saved for testing. 

As it can be seen, the accuracy for both (in case of "random_state=42") is 1.0. 

Iris is not a very complicated dataset, and as it can be seen from the PCA graph, the 3 species are either completely or nearly separable, which leads to accuracy of predictions made to either be 1.0 or near 1.0.

To run the code:
```bash
#Clone this repository
git clone https://github.com/ruhandave19/Projects.git
#Navigate into the project folder
cd Projects
cd iris_classifier
cd iris_accuracy
#Install dependencies 
pip install -r requirements.txt
#Run the script
py iris_acc.py
```

Example output:
```bash
Importing and creating test-train split...
Done
Importing and training decision tree...
Done
Importing and training SVM...
Done
Decision Tree Accuracy: 1.0
SVM Accuracy: 1.0
![Iris PCA Visualization](images/iris_pca.png)
```