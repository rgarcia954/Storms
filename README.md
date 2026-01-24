# Hurricane Data Filter

A Python script for filtering and extracting hurricane data from IBTrACS (International Best Track Archive for Climate Stewardship) CSV files based on specific geospatial and temporal criteria.

## Overview

This tool processes multiple IBTrACS CSV files and filters hurricane records that meet specific criteria including geographic boundaries (focusing on the Florida region), temporal range, and storm classification. The filtered results are compiled into a single CSV file for further analysis.

## Features

- **Batch Processing**: Automatically processes all CSV files in a specified directory
- **Geospatial Filtering**: Filters hurricanes within defined latitude/longitude boundaries
- **Temporal Filtering**: Restricts data to a specific year range (1960-2024)
- **Status Filtering**: Extracts only records classified as hurricanes (HU status)
- **Data Extraction**: Extracts year, month, and day from ISO timestamp
- **Error Handling**: Gracefully handles missing files, malformed data, and processing errors
- **Consolidated Output**: Combines filtered results from multiple files into a single CSV

## Requirements

- Python 3.6+
- pandas

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/hurricane-data-filter.git
cd hurricane-data-filter
```

2. Install required dependencies:
```bash
pip install pandas
```

## Usage

### Basic Usage

Place your IBTrACS CSV files in a directory named `ibtracs` (or specify a different directory), then run:

```bash
python filter_hurricane_data.py
```

### Custom Parameters

You can modify the script to use custom input/output paths:

```python
from filter_hurricane_data import filter_hurricane_data

# Use custom directory and output file
filter_hurricane_data(
    input_directory='my_data_folder',
    output_file='my_filtered_results.csv'
)
```

## Configuration

The script uses the following default filtering parameters:

| Parameter | Value | Description |
|-----------|-------|-------------|
| **Latitude Bounds** | 24.396308° to 31.000968° N | Approximate Florida region |
| **Longitude Bounds** | -87.634938° to -80.031362° E | Approximate Florida region |
| **Year Range** | 1960 - 2024 | Historical to recent data |
| **Status** | HU | Hurricane classification only |

To modify these parameters, edit the constants in the `filter_hurricane_data()` function:

```python
LAT_BOUNDS = (24.396308, 31.000968)
LON_BOUNDS = (-87.634938, -80.031362)
YEAR_BOUNDS = (1960, 2024)
STATUS_TARGET = 'HU'
```

## Output

The script generates a CSV file (`filtered_hurricane_data.csv` by default) containing the following columns:

- `USA_LAT`: Latitude coordinate
- `USA_LON`: Longitude coordinate
- `NAME`: Hurricane name
- `YEAR`: Year of occurrence
- `MONTH`: Month of occurrence
- `DAY`: Day of occurrence
- `USA_STATUS`: Storm classification status
- `USA_WIND`: Maximum sustained wind speed

## Data Source

This script is designed to work with IBTrACS (International Best Track Archive for Climate Stewardship) data, which can be downloaded from:

**NOAA IBTrACS**: https://www.ncei.noaa.gov/products/international-best-track-archive

## Example Output

```
Processing: ibtracs.NA.list.v04r01.csv
Processing: ibtracs.SI.list.v04r01.csv
Success! Filtered results saved to filtered_hurricane_data.csv
Total rows matched: 1247
```

## Error Handling

The script includes robust error handling:
- Validates directory existence before processing
- Handles missing or malformed CSV files gracefully
- Converts data types with error coercion to prevent crashes
- Reports errors for individual files while continuing to process others

## Limitations

- Requires IBTrACS-formatted CSV files with specific column names
- Filters are hardcoded and require script modification to change
- Memory usage scales with the size of input files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data source: NOAA's International Best Track Archive for Climate Stewardship (IBTrACS)
- Inspired by the need for regional hurricane analysis in climate research

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This script is designed for research and educational purposes. Always verify filtered data against original sources for critical applications.