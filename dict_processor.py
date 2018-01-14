import csv
import csv_reader

employees = [{'age': '30', 'name': 'John', 'last_name': 'Doe'}, {'age': '30', 'name': 'Jane', 'last_name': 'Doe'}]


def write_csv_file(filename, output_list):
    # Get the header from the first row
    first_row = output_list[0]
    header_str = first_row.keys()

    with open(filename, 'w') as csv_header_file:
        csv_writer = csv.writer(csv_header_file)
        csv_writer.writerow(header_str)

        # Process the data
        for row in output_list:
            data_str = row.values()
            csv_writer.writerow(data_str)


def main():
    # Call the writer routine. Then use the reader to verify it
    sample_filename = 'CSV with header row.csv'
    write_csv_file(sample_filename, employees)
    csv_reader.read_csv_file(sample_filename)


if __name__ == '__main__':
    main()
