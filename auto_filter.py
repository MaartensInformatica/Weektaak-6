import csv


def filter_request():
    filter_dictionary = {}
    while True:
        input_ = input("Enter the column name you want to filter on.\n")
        input_2 = input("Enter the value(s) of the filter.\n")
        filter_value_list = ([])
        filter_value_list.append(input_2)
        value_loop = True
        while value_loop:
            input_3 = input("Do you want to add another filter? y/n.\n")
            if input_3 == "y":
                input_4 = input("Enter the value(s) of the filter.\n")
                filter_value_list.append(input_4)
                continue
            else:
                value_loop = False
        filter_dictionary[input_] = filter_value_list
        input_5 = input("Do you want to add another column? y/n\n")
        if input_5 == "n":
            break
    return filter_dictionary


def index_setter(dictionary, file):
    index_value_dictionary = {}
    with open(file) as open_file:
        tsv_file = csv.reader(open_file, delimiter='\t')
        tsv_first_line = next(tsv_file)
        print(tsv_first_line)
        for index, element in enumerate(tsv_first_line):
            try:
                if element in dictionary:
                    print("Ja in de dict")
                    index_value_dictionary[index] = dictionary[element]
            except ValueError:
                pass
        return index_value_dictionary


def


if __name__ == '__main__':
    file_ = "tsv.txt"
    var = filter_request()
    print(var)
    var2 = index_setter(var, file_)
    print(var2)

