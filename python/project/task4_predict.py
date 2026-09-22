import pandas as pd
from sklearn.linear_model import LogisticRegression

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
    "Two Year": "Two year",
    "One Year": "One year"
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

df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen', 'Contract']

contract_mapping = {
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2
}
df = df.dropna(subset=['Contract']).reset_index(drop=True)

df['Contract'] = df['Contract'].map(contract_mapping)

X = df[features]
y = df['Churn']

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

print("\n--- Enter Customer Information ---")
user_tenure = int(input("Enter tenure (months): "))
user_monthly_charges = float(input("Enter Monthly Charges: "))
user_total_charges = float(input("Enter Total Charges: "))
user_senior_citizen = int(input("Senior Citizen? (1 = Yes, 0 = No): "))
user_contract = int(input("Contract type (0 = Month-to-month, 1 = One year, 2 = Two year): "))

input_data = pd.DataFrame([{
    'tenure': user_tenure,
    'MonthlyCharges': user_monthly_charges,
    'TotalCharges': user_total_charges,
    'SeniorCitizen': user_senior_citizen,
    'Contract': user_contract
}])

prediction = model.predict(input_data)[0]

print("\n--- Prediction Result ---")
if prediction == 1:
    print("Prediction: This customer is likely to CHURN.")
else:
    print("Prediction: This customer is likely to STAY.")