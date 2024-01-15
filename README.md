# XML to CSV & SQL Converter

This Python script converts XML data to CSV and inserts the data into a SQLite database.

## Prerequisites

Make sure you have Python installed on your system.

## Usage

1. Clone the repository or download the Python script.

2. Run the script.

3. Enter the XML file name when prompted.

4. The script will generate a CSV file and insert the data into an SQLite database.

## Script Details

### xml_to_csv_and_sql(xml_file, csv_file, db_file)

- Parses the specified XML file.
- Extracts headers from the XML data.
- Writes the data to a CSV file.
- Creates an SQLite database and inserts data from the CSV.

### read_csv(csv_file)

- Reads and prints the contents of the generated CSV file.

## Notes

- Ensure that the XML file follows a structure where each record is represented by a nested set of elements under a common parent. I've included two working examples of datasets, one small and one large.

- The script checks for empty values in the XML data and skips rows where all values are empty or blank.

- The generated CSV file and SQLite database will be named based on the input XML file.
