from sklearn.datasets import load_iris

iris = load_iris()

print("Importing and creating train-test split")
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, train_size=0.99)
print("Done!")

print("Importing and training SVC")
from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)
print("Done!")

a="y"
to_predict = []
while a=="y":
    sepal_length = input("Please input the sepal length in cm (for meaningful result, it should be in the range 4-8cm): ")
    to_predict.append(sepal_length)
    sepal_width = input("Please input the sepal width in cm (for meaningful result, it should be in the range 2-4cm): ")
    to_predict.append(sepal_width)
    petal_length = input("Please input the petal length in cm (for meaningful result, it should be in the range 1-7cm): ")
    to_predict.append(petal_length)
    petal_width = input("Please input the petal width in cm (for meaningful result, it should be in the range 0-2.5cm): ")
    to_predict.append(petal_width)

    print(f"The predicted species is: {(iris.target_names[svc.predict([to_predict])])[0]}")

    a = input("Would you like to get another prediction? (y/n) ")
    to_predict.clear()