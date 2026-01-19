import pandas as pd
import os

def filter_hurricane_data(input_directory='ibtracs', output_file='filtered_hurricane_data.csv'):
    """
    Reads all CSVs in a directory, filters for hurricanes in specific 
    geospatial/temporal bounds, and saves the results.
    """
    # Define filtering constants
    LAT_BOUNDS = (24.396308, 31.000968)
    LON_BOUNDS = (-87.634938, -80.031362)
    YEAR_BOUNDS = (1960, 2024)
    STATUS_TARGET = 'HU'
    
    # Columns requested for final output
    columns_to_save = ['USA_LAT', 'USA_LON', 'NAME', 'YEAR', 'MONTH', 'DAY', 'USA_STATUS', 'USA_WIND']
    
    all_data = []

    # 1. Check if directory exists
    if not os.path.exists(input_directory):
        print(f"Error: Directory '{input_directory}' not found.")
        return

    # 2. Iterate through all CSV files in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_directory, filename)
            print(f"Processing: {filename}")
            
            try:
                # Load CSV (low_memory=False handles mixed types common in IBTrACS)
                df = pd.read_csv(file_path, low_memory=False)
                
                # Pre-processing: Extract Year, Month, and Day from ISO_TIME
                if 'ISO_TIME' in df.columns:
                    df['ISO_TIME'] = pd.to_datetime(df['ISO_TIME'], errors='coerce')
                    df['YEAR'] = df['ISO_TIME'].dt.year
                    df['MONTH'] = df['ISO_TIME'].dt.month
                    df['DAY'] = df['ISO_TIME'].dt.day

                # Ensure coordinate columns are numeric for comparison
                df['USA_LAT'] = pd.to_numeric(df['USA_LAT'], errors='coerce')
                df['USA_LON'] = pd.to_numeric(df['USA_LON'], errors='coerce')

                # 3. Apply the specific filtering conditions
                mask = (
                    (df['USA_STATUS'].astype(str).str.strip() == STATUS_TARGET) &
                    (df['USA_LAT'] >= LAT_BOUNDS[0]) & (df['USA_LAT'] <= LAT_BOUNDS[1]) &
                    (df['USA_LON'] >= LON_BOUNDS[0]) & (df['USA_LON'] <= LON_BOUNDS[1]) &
                    (df['YEAR'] >= YEAR_BOUNDS[0]) & (df['YEAR'] <= YEAR_BOUNDS[1])
                )
                
                filtered_df = df[mask].copy()
                
                # Subset only the requested columns
                # (Intersection ensures we don't crash if a file is missing a column)
                cols_to_keep = [c for c in columns_to_save if c in filtered_df.columns]
                all_data.append(filtered_df[cols_to_keep])

            except Exception as e:
                print(f"Skipping {filename} due to error: {e}")

    # 4. Concatenate all filtered results and save to a new CSV
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        final_df.to_csv(output_file, index=False)
        print(f"Success! Filtered results saved to {output_file}")
        print(f"Total rows matched: {len(final_df)}")
    else:
        print("No matching hurricane records were found in the provided files.")

if __name__ == "__main__":
    filter_hurricane_data()