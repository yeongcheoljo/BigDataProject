import pandas as pd
import numpy as np

# Replace 'your_file.csv' with the path to your CSV file
file_path = "/content/노선별 이용량 23-combine.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path, encoding='utf-8-sig')

# Replace this list with the column names you want to check
columns_to_check = ["노선", "기종점", "월", "정류장순번", "정류장", "이용자유형"]

# Extract rows where any of the specified columns have null values
rows_with_nulls_in_columns = df[df[columns_to_check].isnull().any(axis=1)]

index_numbers_with_nulls = rows_with_nulls_in_columns.index

# Print the index numbers
print(f"Index numbers of rows with null values in columns {columns_to_check}:")
print(index_numbers_with_nulls)

df['노선'] = df['노선'].replace('합계', np.nan)

df.loc[index_numbers_with_nulls, '이용자유형'] = '합계'

df[columns_to_check] = df[columns_to_check].fillna(method='bfill')

df.to_csv('노선별 이용량 전처리 23-combine.csv', index=False, encoding='utf-8-sig')
