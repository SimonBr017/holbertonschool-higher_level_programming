#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary)
    for str in new_list:
        print("{:s}: {}".format(str, a_dictionary[str]))
