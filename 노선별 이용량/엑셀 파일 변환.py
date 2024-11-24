import pandas as pd

# Upload the Excel file
from google.colab import files
uploaded = files.upload()  # Choose your Excel file from your local system

# Load the Excel file
excel_file = list(uploaded.keys())[0]  # Get the uploaded file name
df = pd.read_excel(excel_file)  # Read the first sheet of the Excel file

# Save as a CSV file
csv_file = excel_file.replace('.xlsx', '.csv')  # Replace extension
df.to_csv(csv_file, index=False, encoding='utf-8-sig')  # Save without the index column

# Download the CSV file
files.download(csv_file)  # Download the converted file
