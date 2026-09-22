import pandas as pd

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

print("--- Cleaned DataFrame Shape (rows, columns) ---")
print(df.shape)
print()

print("--- Missing Value Counts Per Column ---")
print(df.isnull().sum())