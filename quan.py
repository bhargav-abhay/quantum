import pandas as pd
import os

# List of file paths to combine
file_paths = [
    r'C:\Users\ABHAY TRIPATHI\OneDrive\Desktop\javascript\quantium-starter-repo\data\daily_sales_data_0.csv',
    r'C:\Users\ABHAY TRIPATHI\OneDrive\Desktop\javascript\quantium-starter-repo\data\daily_sales_data_1.csv',
    r'C:\Users\ABHAY TRIPATHI\OneDrive\Desktop\javascript\quantium-starter-repo\data\daily_sales_data_2.csv'
]

# Create an empty list to hold the dataframes
dfs = []

# Loop through the file paths and read each CSV file
for file in file_paths:
    if os.path.exists(file):
        df = pd.read_csv(file)
        dfs.append(df)
    else:
        print(f"File not found: {file}")

# Concatenate all dataframes in the list
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)

    # Display the first 5 rows and info of the combined DataFrame
    print("Combined DataFrame head:")
    print(combined_df.head())
    print("\nCombined DataFrame info:")
    print(combined_df.info())

    # Save the combined DataFrame to a new CSV file
    output_file_name = 'combined_sales_data.csv'
    combined_df.to_csv(output_file_name, index=False)
    print(f"\nSuccessfully combined the files and saved to {output_file_name}")
else:
    print("No files were found to combine.")