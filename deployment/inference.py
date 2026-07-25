import joblib
import pandas as pd
import os

def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "customer_churn_model.pkl"))
    scaler = joblib.load(os.path.join(model_dir, "scaler.pkl"))
    return model, scaler


def input_fn(request_body, request_content_type):

    if request_content_type == "text/csv":
        data = pd.read_csv(pd.compat.StringIO(request_body), header=None)
        return data

    raise ValueError("Unsupported content type")


def predict_fn(input_data, model):

    model, scaler = model

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    return prediction


def output_fn(prediction, content_type):

    return str(prediction.tolist())