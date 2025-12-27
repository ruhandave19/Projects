from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

print("Importing and creating test-train split...")
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)
print("Done")

print("Importing and training decision tree...")
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=3, random_state=42, criterion="gini")
dt.fit(X_train, y_train)
print("Done")

print("Importing and training SVM...")
from sklearn.svm import SVC
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train, y_train)
print("Done")

from sklearn.metrics import accuracy_score
print("Decision Tree Accuracy:", accuracy_score(y_test, dt.predict(X_test)))
print("SVM Accuracy:", accuracy_score(y_test, svm.predict(X_test)))

from sklearn.decomposition import PCA
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")

X_reduced = PCA(n_components=3).fit_transform(iris.data)

scatter = ax.scatter(X_reduced[:,0], X_reduced[:,1], X_reduced[:,2], c=iris.target)
ax.set(title="Iris Reduced to 3 Dimensions", xlabel="First Principal Component", ylabel="Second Principal Component", zlabel="Third Principal Component")
legend = ax.legend(scatter.legend_elements()[0], iris.target_names.tolist(), loc="upper right", title="Classes")
ax.add_artist(legend)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])

plt.show()