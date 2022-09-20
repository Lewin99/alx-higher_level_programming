#!/usr/bin/python3
def element_at(my_list, idx):
    if idx <0:
        print("none")
    elif idx > len(my_list):
        print("none")
    else:
        print("Element at index {:d} is {}".format(idx,my_list[idx]))
