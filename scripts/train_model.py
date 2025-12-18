import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def main():
    dataset = load_iris()
    X = dataset.data.tolist()
    y = [str(dataset.target_names[i]).capitalize() for i in dataset.target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Accuracy: {accuracy:.4f}")
    joblib.dump(model, 'app/model.joblib')


if __name__ == "__main__":
    main()
