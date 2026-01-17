import os
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

# Function to read all CSV files in a directory and filter rows based on pertinent data
# Save only the specified columns to a new CSV
def filter_and_save_hurricane_data(input_directory, output_file, columns_to_save):
    # Create an empty list to store the filtered data
    filtered_data = []

    # Loop through all files in the directory
    for filename in os.listdir(input_directory):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            file_path = os.path.join(input_directory, filename)
            
            # Read the CSV file
            df = pd.read_csv(file_path, dtype=str)

            # Convert the USA_TIME column to a datetime object
            df['ISO_TIME'] = pd.to_datetime(df['ISO_TIME'], format='%m/%d/%y %H:%M')

            # Create new columns for YEAR, MONTH, and DAY
            df['YEAR'] = df['ISO_TIME'].dt.strftime('%y')  # Extract the year
            df['MONTH'] = df['ISO_TIME'].dt.strftime('%m')  # Extract the month
            df['DAY'] = df['ISO_TIME'].dt.strftime('%d')    # Extract the day

            df["USA_LAT_DEC"] = pd.to_numeric(df["USA_LAT"], errors="coerce")
            df["USA_LON_DEC"] = pd.to_numeric(df["USA_LON"], errors="coerce")
            df["YEAR_DEC"] = pd.to_numeric(df["YEAR"], errors="coerce")

            #Stipulate pertinent columns to parse
            filtered_rows = df[
                            (df['USA_STATUS'].str.contains('HU', case=False, na=False)) &
                            (df['USA_LAT_DEC'].between(24.396308, 31.000968)) &
                            (df['USA_LON_DEC'].between(-87.634938, -80.031362)) &
                            (df['YEAR_DEC'].between(1960, 2024))
            ]

            # Keep only the specified columns
            filtered_rows = filtered_rows[columns_to_save]
            
            # Append the filtered rows to the list
            filtered_data.append(filtered_rows)

    # Concatenate all the filtered rows into a single DataFrame
    if filtered_data:
        result_df = pd.concat(filtered_data, ignore_index=True)
        
        # Save the result to a new CSV file
        result_df.to_csv(output_file, index=False)
        print(f"Filtered data saved to {output_file}")
    else:
        print("No matching data found.")

# Function to convert a string to a date and format output to show only month, day, and year
def convert_to_date(date_string, format_string="%Y-%m-%d"):
    try:
        # Convert string to datetime object
        date_time_obj = datetime.strptime(date_string, format_string)
        
        # Format the output to show only month, day, and year
        date_only = date_time_obj.strftime("%m-%d-%Y")
        print("Formatted date:", date_only)
        return date_only
    except ValueError as e:
        print("Error:", e)
        return None


# Main
input_directory = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/ibtracs'
#input_directory = '.\ibtracs'
output_file = 'filtered_hurricane_data.csv'
columns_to_save = ['USA_LAT_DEC', 'USA_LON_DEC', 'NAME', 'YEAR_DEC', 'MONTH', 'DAY', 'USA_STATUS', 'USA_WIND']

filter_and_save_hurricane_data(input_directory, output_file, columns_to_save)