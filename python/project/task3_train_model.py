import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("files/csv/churnguard_data.csv")

df = df.drop(columns=["customerID"], errors="ignore")

df = df.drop_duplicates()

df["gender"] = df["gender"].str.strip()
df["PaymentMethod"] = df["PaymentMethod"].str.strip()

for col in ["Churn", "PhoneService", "PaperlessBilling"]:
    df[col] = df[col].str.strip().str.title()

contract_key = {
    "month-to-month": "Month-to-month",
    "month to month": "Month-to-month",
    "Monthly": "Month-to-month",
    "2 year": "Two year",
    "two year": "Two year",
    "1 year": "One year",
    "one year": "One year",
}

df["Contract"] = df["Contract"].replace(contract_key)

internet_service_key = {
    "fiber optic": "Fiber optic",
    "dsl": "DSL",
    "no": "No"
}

df["InternetService"] = df["InternetService"].replace(internet_service_key)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce")
df = df[df["tenure"] > 0]

df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")
df = df[(df["MonthlyCharges"] >= 10) & (df["MonthlyCharges"] <= 200)]

df["MonthlyCharges"] = df["MonthlyCharges"].fillna(df["MonthlyCharges"].mean())
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].mean())
df["tenure"] = df["tenure"].fillna(round(df["tenure"].median()))

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

categorical_cols = [
    "gender",
    "PhoneService",
    "InternetService",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Test Set Accuracy: {accuracy:.4f}\n")

print("--- Classification Report ---")
print(classification_report(y_test, y_pred, target_names=["Stay", "Churn"]))