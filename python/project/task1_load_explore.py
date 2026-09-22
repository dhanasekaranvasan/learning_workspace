import pandas

df = pandas.read_csv("files/csv/churnguard_data.csv")

print("--- Dataset Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

print("--- First 5 Rows ---")
print(df.head(), "\n")

print("--- Data Info & Types ---")
df.info()
print()

print("--- Missing Values per Column ---")
print(df.isnull().sum(), "\n")

print("--- Duplicate Rows ---")
print(f"Number of duplicate rows: {df.duplicated().sum()}\n")

print("--- Value Counts: Churn ---")
print(df["Churn"].value_counts(dropna=False), "\n")

print("--- Unique Values: Contract ---")
print(df["Contract"].unique())