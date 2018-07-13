#!/usr/bin/env python

items = 5

# basic definintion
def main():
    print("hello world")
    print("What is the __name__ value ?? {}".format(__name__))

# while
def count_def():
    count = 0
    while count < items:
        print(count)
        count += 1

# if
def if_def():
    count = 0
    value_to_find = 2

    while count < items:
        if count == value_to_find:
            print("Value {} found".format(count))
        else:
            print("Value {} is different from {}".format(count,value_to_find))
        count += 1

# list
def list_def():
    my_list = []
    count = 0
    while count < items:
        print(count)
        my_list.append(count)
        count += 1
    
    print(my_list)

# file / open
def write_to_file_def():
    my_list = []
    count = 0
    while count < items:
        print(count)
        my_list.append(count)
        count += 1
    
    print(my_list)

    filename = open("output.txt","a")
    print(my_list, file = filename)


if __name__ == "__main__":
    # pass
    main()
    count_def()
    if_def()
    list_def()
    write_to_file_def()


