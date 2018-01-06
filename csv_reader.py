import csv

def read_csv_file(filename):

    with open(filename, 'r+') as csv_file:
        reader = csv.reader(csv_file)

        read_lst = list()
        for read_str in reader:
            print(read_str)

write_lst = [['1','2','3'], ['4','5','6']]
def write_csv_file(filename, data_lst):
    # Define the data


    with open(filename, 'w+') as csv_write:
        writer = csv.writer(csv_write)

        for row in data_lst:
            writer.writerow(row)

# Let's see what we wrote
def test_csv_read_write():

    csv_file_name = 'sample_write.csv'
    write_csv_file(csv_file_name)

    print "FileName: ", csv_file_name
    print "Contents: "
    read_csv_file(csv_file_name)

def main():
    # Read number of columns user wants and create a list with that many columns
    columns = int(input('How many columns per row ?'))
    keep_going = True

    generated_lst = list()
    col = list()
    col_limit = 0
    csv_file_name = 'row_col.csv'

    while keep_going:
        col = ["Colum: " + str(col_indx + 1) for col_indx in range(col_limit, col_limit + columns)]
        print(col_limit, col_limit + columns)
        col_limit += columns

        generated_lst.append(col)

        if (raw_input("Keep Going? (Y/N)").lower()) != 'y':
            keep_going = False

        print('Current list: ', generated_lst)
        write_csv_file(csv_file_name, generated_lst)
        read_csv_file(csv_file_name)

if __name__ == '__main__':
    main()

