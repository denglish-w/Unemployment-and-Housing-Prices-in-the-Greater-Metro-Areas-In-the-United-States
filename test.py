import pandas as pd
from src.cleaning import DataCleaner

df_emp_raw = pd.read_csv('data/raw/ssamatab1.csv', skiprows=2).dropna()

df_house_raw = pd.read_csv('data/raw/hpi_po_metro.csv')

emp_cleaner = DataCleaner(df_emp_raw)
house_cleaner = DataCleaner(df_house_raw)

emp_cleaner.rename_emp()
df_emp = emp_cleaner.df

emp_cleaner.drop_n_values()
df = emp_cleaner.df

print(df)