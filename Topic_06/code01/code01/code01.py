#!/usr/bin/env python

my_list = ["servidor1","servidor2","servidor3","servidor4","servidor5","servidor6","servidor7","servidor8"]

# Definition to show the list content
def show_for():
    for x in my_list:
        print(x)

# Definition to show the list content and test one by one
def show_for_if():
    for x in my_list:
        if x == "servidor3":
            print(x)

# Definition using while true *forever* :-)
def show_while():
    while True:
        aux = input("Value: ")
        if aux == "-999":
            break

# Let's read the Conf File
def reading_conf_file():
    import re
    CONF_FILE = "code01/code01/server.conf"

    f = open(CONF_FILE, "r")

    for line_file in f:
        if re.findall("^server", line_file):
            fields_line = re.split("=", line_file)
            SERVER = fields_line[1].strip()

        if re.findall("^user", line_file):
            fields_line = re.split("=", line_file)
            USER = fields_line[1].strip()

        if re.findall("^password", line_file):
            fields_line = re.split("=", line_file)
            PASSWORD = fields_line[1].strip()

    print("Server ....: ", SERVER)
    print("User ......: ", USER)
    print("Password ..: ", PASSWORD)

if __name__ == "__main__":
    pass
    #show_for()
    #show_for_if()
    #show_while()
    reading_conf_file()