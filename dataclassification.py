from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("=" * 60)
print("      IRIS FLOWER CLASSIFICATION USING KNN")
print("           DecodeLabs AI Internship")
print("=" * 60)

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Information")
print("-" * 30)
print("Total Samples :", len(X))
print("Total Features:", len(iris.feature_names))
print("Classes       :", list(iris.target_names))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Performance")
print("-" * 30)
print(f"Accuracy Score : {accuracy * 100:.2f}%")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

print("\n" + "=" * 60)
print("       USER FLOWER PREDICTION SYSTEM")
print("=" * 60)

while True:

    choice = input("\nDo you want to predict a flower? (yes/no): ").lower()

    if choice == "no":
        print("\nThank you for using the classifier!")
        break

    if choice != "yes":
        print("Please enter yes or no.")
        continue

    try:
        sepal_length = float(input("Sepal Length (cm): "))
        sepal_width = float(input("Sepal Width (cm): "))
        petal_length = float(input("Petal Length (cm): "))
        petal_width = float(input("Petal Width (cm): "))

        user_data = [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]]

        user_data_scaled = scaler.transform(user_data)

        prediction = model.predict(user_data_scaled)

        flower_name = iris.target_names[prediction[0]]

        print("\nPredicted Flower Type:", flower_name.upper())

    except ValueError:
        print("Invalid input. Please enter numeric values only.")