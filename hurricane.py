import os
import csv

# Function to read all CSV files in a directory and print pertinent hurricane data in Florida
def print_hurricane_years_in_fl(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            
            # Open the CSV file
            with open(file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                
                # Loop through rows in the CSV file
                for row in csv_reader:
                    # Check if the STATE column equals 'FLORIDA'
                    if row['STATE'].upper() == 'FLORIDA' and row['EVENT_TYPE'] == 'Hurricane (Typhoon)':
                        # Print the YEAR of the storm
                     #   print(f"Year: {row['YEAR']}, File: {filename}")
                        print(f"Year: {row['YEAR']}, Month: {row['MONTH_NAME']}, File: {filename}")

# Main code
# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/50s'
directory_path = '.\\50s'
print_hurricane_years_in_fl(directory_path)

print()

# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/60s'
directory_path = '.\\60s'
print_hurricane_years_in_fl(directory_path)

print()

# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/70s'
directory_path = '.\\70s'
print_hurricane_years_in_fl(directory_path)

print()

# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/80s'
directory_path = '.\\80s'
print_hurricane_years_in_fl(directory_path)

print()

# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/90s'
directory_path = '.\\90s'
print_hurricane_years_in_fl(directory_path)

print()

# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/00s'
directory_path = '.\\00s'
print_hurricane_years_in_fl(directory_path)

print()

# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/10s'
directory_path = '.\\10s'
print_hurricane_years_in_fl(directory_path)

print()

# directory_path = '/Users/rudygarcia/Library/CloudStorage/OneDrive-Personal/Documents/Family/Rudy/Storms/20s'
directory_path = '.\\20s'
print_hurricane_years_in_fl(directory_path)

print()
