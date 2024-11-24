import pandas as pd
import os

# Set folder path
folder_path = "/content"
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Debugging: Check detected filesprint("Detected files:", csv_files)

# Sort files to process them in order
csv_files.sort()

# Combine all CSV files
dataframes = []
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    print(f"Processing file: {file_path}")
    try:
        df = pd.read_csv(file_path, encoding='UTF-8-SIG')  # Change encoding based on detected type
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Merge all DataFramesif dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Save the combined CSV
    output_file = "정류장 이용량 23-combine.csv"
    combined_df.to_csv(output_file, index=False, encoding='utf-8-sig')  # utf-8-sig for Excel compatibility
    print(f"Data combined and saved to {output_file}")
else:
    print("No valid files to combine.")
