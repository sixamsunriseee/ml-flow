from app.predict import predict


def test_predict():
    assert predict([5.1, 3.5, 1.4, 0.2]) == "Setosa"
