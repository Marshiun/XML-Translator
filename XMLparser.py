import sqlite3
from lxml import etree
import csv

def xml_to_csv_and_sql(xml_file, csv_file, db_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Extract headers from the XML
    headers_set = {element.tag for element in root.iter()}
    ordered_headers = list(headers_set)

    # Write data to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerow(ordered_headers)

        for row in root.xpath('.//*'):
            data = [row.find(header).text.strip() if row.find(header) is not None and row.find(header).text is not None and row.find(header).text.strip() != '' else "" for header in ordered_headers]

            # If all values in the row are empty or blank, skip the row
            if any(val != '' for val in data):
                writer.writerow(data)

    # Convert CSV values to SQL Database
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Create table in the database
    create_table_query = f"CREATE TABLE IF NOT EXISTS xml_data ({', '.join([f'{header} TEXT' for header in ordered_headers])});"
    cursor.execute(create_table_query)

    with open(csv_file, 'r', encoding='utf-8') as input:
        reader = csv.reader(input)
        next(reader)  # Skip header row
        rows = [row for row in reader]

        insert_query = f"INSERT INTO xml_data VALUES ({', '.join(['?' for _ in ordered_headers])});"
        cursor.executemany(insert_query, rows)

    connection.commit()
    connection.close()

# Read CSV file 
def read_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Prompt user for XML file name
try:
    xml_file_name = input("Enter the XML file name: ")
    name = xml_file_name.removesuffix('.xml')
    csv_file_path = f'{name}.csv'  
    db_file_path = f'{name}.db'

    xml_to_csv_and_sql(xml_file_name, csv_file_path, db_file_path)
    print(f"CSV file saved at: {csv_file_path}")
    print(f"Data inserted into SQL database at: {db_file_path}")

    # # preview CSV file
    # csv_file_path = f'{name}.csv'
    # read_csv(csv_file_path)

except:
    print(f"An error occurred.")