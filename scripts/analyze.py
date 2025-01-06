import os
import pandas as pd

# Define the folder where the TXT files are located
data_folder = r'C:\Users\Avinash rai\Downloads\data'  # Update this path as necessary

# Initialize an empty list to hold the data from all TXT files
all_data = []

# List the files in the folder to check for the existence of year-based files
file_names = os.listdir(data_folder)
print(f"Files in the directory: {file_names}")  # Debugging line to check files

# Iterate over the files in the folder and process the year-based TXT files
for file_name in file_names:
    if file_name.endswith('.txt'):  # Process only TXT files
        year = file_name[3:7]  # Extract the year from the file name (e.g., 'yob2000.txt' -> '2000')
        file_path = os.path.join(data_folder, file_name)
        print(f"Reading file: {file_path}")  # Debugging line
        
        # Read the file into a DataFrame, assuming it's comma-separated
        try:
            df = pd.read_csv(file_path, header=None, names=['Name', 'Sex', 'Count'], encoding='utf-8')
            # Add a 'Year' column to each record
            df['Year'] = year
            all_data.append(df)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Check if any files were successfully read
if not all_data:
    print("No TXT files were found or read.")
else:
    # Concatenate all data into a single DataFrame
    data = pd.concat(all_data, ignore_index=True)

    # Display the shape and first few rows of the data
    print(f"Data shape: {data.shape}")  # This will show how many rows and columns are there
    print(f"First few rows:\n{data.head()}")

    # Drop any rows with missing values (if any)
    data.dropna(inplace=True)

    # Display the cleaned data
    print(f"Cleaned data preview:\n{data.head()}")
