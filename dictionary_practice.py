import os
import argparse
import csv
import random

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--columns",
                    type=int,
                    default=5,
                    metavar="<number of columns>",
                    help="Number of columns to create in the dictionary")
parser.add_argument("-r", "--rows",
                    type=int,
                    default=5,
                    metavar="<number of rows>",
                    help="Number of rows to create in the dictionary")
parser.add_argument("-o", "--outfile",
                    type=str,
                    default="C:\Temp",
                    metavar="<number of rows>",
                    help="Number of rows to create in the dictionary")
parser.add_argument("-v", "--verbose",
                    help="Increase output verbosity",
                    action="store_true")
args = parser.parse_args()

dictionary_data = {}
dictionary_list = []
fieldnames = []

def create_dictionary_size(columns):
    for _ in range(0, columns):
        key = "key" + str(_ + 1)
        dictionary_data[key] = int()

def generate_dictionary_data():
    for key in dictionary_data:
        dictionary_data[key] = random.randint(1,9999)
        # new_data = dictionary_data
    return dict(dictionary_data)

def generate_list(rows):
    for _ in range(rows):
        dictionary_list.append(generate_dictionary_data())

# def create_csv(path):

#     with open(path, "w", newline="") as csvfile:
    
#         # Establish fieldnames from number keys
#         for key in dictionary_list[0]:
#             fieldnames.append(key)
        
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()

#         for item in dictionary_list:
#             writer.writerow(item)

def main():

    if args.rows:
        rows = args.rows
        if args.verbose == True:
            if args.rows < 2:
                plural = ""
            else:
                plural = "s"
            print("\nVERBOSE: Row{}: {}".format(plural, args.rows))
    
    if args.columns:
        columns = args.columns
        if args.verbose == True:
            if args.columns < 2:
                plural = ""
            else:
                plural = "s"
            print("\nVERBOSE: Column{}: {}".format(plural, args.columns))

    if args.outfile:
        outfile = args.outfile
        if args.verbose == True:
            print("VERBOSE: Output file: {}".format(outfile))

    # Create dictionary size
    create_dictionary_size(columns)

    # # Create a list of dictionaries of the size from passed argment (integer)
    generate_list(rows)

    if args.verbose == True:
        print("\nGenerated dictionary list:\n{}\n".format(dictionary_list))

    # Save generated list of dictionaries to csv file
    # create_csv(str(sys.argv[3]))

if __name__ == "__main__":
    main()