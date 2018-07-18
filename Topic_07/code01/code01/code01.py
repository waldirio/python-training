#!/usr/bin/env python


def simple_read_json():
    import json

    file_content = open("code01/code01/file.json","r")
    json_content = json.load(file_content)

    if json_content:
        for obj in json_content['users']:
            print(obj['name'])
            print(obj['age'])
            print(obj['city'])


def formatted_json_output():
    import json

    file_content = open("code01/code01/file.json","r")
    json_content = json.load(file_content)

    if json_content:
        for obj in json_content['users']:
            print("User Name ......: ", obj['name'])
            print("Your Age .......: ", obj['age'])
            print("Your City ......: ", obj['city'])
            print("")


def formatted_json_output_with_count():
    import json

    file_content = open("code01/code01/file.json","r")
    json_content = json.load(file_content)

    total_elements = len(json_content['users'])
    print("There are {} elements USERS on the file.".format(total_elements))
    print("")

    if json_content:
        for obj in json_content['users']:
            print("User Name ......: ", obj['name'])
            print("Your Age .......: ", obj['age'])
            print("Your City ......: ", obj['city'])
            print("")


def json_estados():
    import json

    file_content = open("code01/code01/Estados.json","r")
    json_content = json.load(file_content)

    pass
    """
    TODO - HOMEWORK
        - Print the total # of States
        - Print the name of all States
        - Generate a file with the Initials *each one per line*
    """

def json_cidades():
    import json

    file_content = open("code01/code01/Cidades.json","r")
    json_content = json.load(file_content)

    pass
    """
    TODO - HOMEWORK
        - Print the total # of Cities
        - Print the total of Cities per State *at this moment use just the State code*
        - Generate a file with the Initials *each one per line*
    """

def json_city_state_full():
    pass
    """
    Please implement here the code to read the Cidades.json and Estados.json, then 
    create the function to generate the result as below
    State - # of Cities
    RJ - 92
    AP - 16
    ...


    $ grep "\"19\"" Cidades.json  | grep Estado | wc -l
    92
    $

    $ grep "\"4\"" Cidades.json  | grep Estado | wc -l
    16
    $ 
    """

if __name__ == "__main__":
    pass
    #simple_read_json()
    #formatted_json_output()
    #formatted_json_output_with_count()
    #json_estados()
    #json_cidades()
    #json_city_state_full()