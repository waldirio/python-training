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

    print("")
    pass

    """ TODO - HOMEWORK
        - Print the total # of States
        - Print the name of all States
        - Generate a file with the Initials *each one per line*
    """

    # Print the total # of States
    total_number_of_estados = len(json_content)
    print("Total State number is: {}".format(total_number_of_estados))

    # Print the name of all States
    for each_name in json_content:
        print(each_name['Nome'])

    #  Generate a file with the Initials *each one per line*
    filename = open("code01/code01/states_result.log","w")
    for each_name in json_content:
        print(each_name['Nome'],file = filename)


def json_cidades():
    import json

    file_content = open("code01/code01/Cidades.json","r")
    json_content = json.load(file_content)

    print("")
    pass
    """ TODO - HOMEWORK
        - Print the total # of Cities
        - Print the total of Cities per State *at this moment use just the State code*
        - Generate a file with the Cities names *each one per line*
    """

    # Print the total # of Cities
    total_number_of_cidades = len(json_content)
    print("Total Cities number is: {}".format(total_number_of_cidades))

    # Print the total of Cities per State *at this moment use just the State code*
    temp_city_list = []
    temp_city_list_final = []
    for each_name in json_content:
        temp_city_list.append(each_name['Estado'])

    # Temporary list with the State codes    
    temp_city_list_final = list(set(temp_city_list))
    # print(temp_city_list_final)

    # Initializing the counter to zero
    count = 0
    
    # Loop using the Code State and for each one checking the complete State list just to count
    # the number of entries per State
    for each_city_code in temp_city_list_final:
        for each_city_name in json_content:
            if each_city_code == each_city_name['Estado']:
                count = count + 1
        
        print("City code: {} -- # of Cities: {}".format(each_city_code,count))
        count = 0


    #  Generate a file with the Cities names *each one per line*
    filename = open("code01/code01/cities_result.log","w")
    for each_name in json_content:
        print(each_name['Nome'],file = filename)



def json_city_state_full():
    pass
    """
    Please implement here the code to read the Cidades.json and Estados.json, then 
    create the logic to generate the result as below
    State , # of Cities
    RJ , 92
    AP , 16
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
    #Isimple_read_json()
    #formatted_json_output()
    #formatted_json_output_with_count()
    #json_estados()
    #json_cidades()
    #json_city_state_full()