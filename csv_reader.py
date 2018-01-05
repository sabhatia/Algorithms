import csv

def read_csv_file(filename):

    with open(filename, 'r+') as csv_file:
        reader = csv.reader(csv_file)

        read_lst = list()
        for read_str in reader:
            print(read_str)

def write_csv_file(filename):
    # Define the data
    write_lst = [['1','2','3'], ['4','5','6']]

    with open(filename, 'w+') as csv_write:
        writer = csv.writer(csv_write)

        for row in write_lst:
            writer.writerow(row)

# Let's see what we wrote
csv_file_name = 'sample_write.csv'
write_csv_file(csv_file_name)

print "FileName: ", csv_file_name
print "Contents: "
read_csv_file(csv_file_name)