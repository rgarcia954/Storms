import os
import pandas as pd

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
            
            df = pd.read_csv(file_path)

            #Stipulate pertinent columns to parse
            filtered_rows = df[(df['USA_STATUS'].str.contains('HU', case=False, na=False))]
            
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

# Main
input_directory = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/ibtracs'
output_file = 'filtered_hurricane_data.csv'
columns_to_save = ['USA_LAT', 'USA_LON', 'NAME', 'ISO_TIME', 'USA_STATUS', 'USA_WIND']

filter_and_save_hurricane_data(input_directory, output_file, columns_to_save)