import joblib


model = joblib.load('app/model.joblib')


def predict(x: list[float]) -> str:
    return model.predict([x])[0]
