# Customer Churn Prediction using Machine Learning and Amazon SageMaker

## Project Overview

Customer churn prediction is one of the most important business problems in the telecom industry. This project predicts whether a customer is likely to leave the service based on customer demographics, account information, and service usage patterns.

The project demonstrates a complete end-to-end Machine Learning workflow, including data preprocessing, feature engineering, model training, hyperparameter tuning, model evaluation, and deployment using Amazon SageMaker.

---

## Project Architecture

Customer Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Feature Engineering
        │
        ▼
Train-Test Split
        │
        ▼
Feature Scaling
        │
        ▼
Random Forest Model
(GridSearchCV Hyperparameter Tuning)
        │
        ▼
Model Evaluation
        │
        ├── Accuracy
        ├── Classification Report
        ├── Confusion Matrix
        └── ROC Curve
        │
        ▼
Save Model (.pkl)
        │
        ▼
Upload Model to Amazon S3
        │
        ▼
Deploy Model using Amazon SageMaker
        │
        ▼
Real-Time Customer Churn Prediction

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Amazon S3
- Amazon SageMaker
- Jupyter Notebook

---

## Machine Learning Workflow

### Data Collection

- Customer Churn Dataset

### Data Preprocessing

- Handling missing values
- Label Encoding
- Feature Scaling
- Train-Test Split

### Model Building

- Random Forest Classifier

### Hyperparameter Tuning

- GridSearchCV

### Model Evaluation

- Accuracy Score
- Classification Report
- Confusion Matrix
- ROC Curve
- AUC Score

### Model Saving

- Saved using Joblib

### Cloud Deployment

- Uploaded model.tar.gz to Amazon S3
- Deployed using Amazon SageMaker
- Real-time prediction endpoint

---

## Project Structure

```
customer-churn-prediction/

│── customer_churn.ipynb
│── inference.py
│── requirements.txt
│── README.md
│── .gitignore
│── LICENSE

├── dataset/
│     └── customer_churn.csv

├── models/
│     ├── customer_churn_model.pkl
│     └── scaler.pkl

├── deployment/
│     └── model.tar.gz

├── images/
│     ├── confusion_matrix.png
│     ├── roc_curve.png
│     └── feature_importance.png
```

---

## Model Performance

| Metric | Result |
|---------|--------|
| Accuracy | XX% |
| Precision | XX |
| Recall | XX |
| F1 Score | XX |
| ROC-AUC | XX |

Replace the values above with your actual results.

---

## Results

The Random Forest Classifier successfully predicts customer churn with high accuracy.

The model was evaluated using:

- Classification Report
- Confusion Matrix
- ROC Curve
- AUC Score

The trained model was packaged and prepared for deployment using Amazon SageMaker.

---

## Screenshots

### Confusion Matrix

Add screenshot here.

---

### ROC Curve

Add screenshot here.

---

### Feature Importance

Add screenshot here.

---

## Future Improvements

- Compare multiple machine learning algorithms
- Perform feature selection
- Build an interactive Streamlit dashboard
- Automate the deployment pipeline
- Implement CI/CD using AWS CodePipeline

---

## Author

**Rathish R**

- Data Science Consultant
- Python | Machine Learning | AWS SageMaker | SQL | Power BI
