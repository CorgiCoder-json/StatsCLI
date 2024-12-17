import csv
import os
import math
import copy

file_contents = {}
current_contents = file_contents
file_path_keys = []

def read_file(file_path):
    with open(file_path, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            print(line)

def update_dir(file_dict, keys, new_dir):
    if len(keys) == 1 or len(file_dict[keys[0]].keys()) == 0:
        file_dict[keys[0]].update({new_dir: {}})
        return 0
    next_set = file_dict[keys[0]]
    keys.pop(0)
    return update_dir(next_set, keys, new_dir)

def return_dir(file_dict, keys):
    if len(keys) == 1 or len(file_dict[keys[0]].keys()) == 0:
        return file_dict[keys[0]]
    next_set = file_dict[keys[0]]
    keys.pop(0)
    return return_dir(next_set, keys)

if __name__ == "__main__":
    user_in = ''
    current_dir = "/"
    while user_in != 'q':
        user_in = input(current_dir + "> ")
        command = user_in.split()
        if command[0] == "listdir":
            print(list(current_contents.keys()))
        elif command[0] == "makedir":
            try:
                copied_keys = copy.deepcopy(file_path_keys)
                if len(file_path_keys) > 0:
                    update_dir(file_contents, copied_keys, command[1])
                else:
                    file_contents.update({command[1]: {}})
            except Exception as err:
                print(err)
                print("Invalid command input!")
        elif command[0] == "changedir":
            try:
                if command[1] == "<-":
                    file_path_keys.pop()
                    copied_keys = copy.deepcopy(file_path_keys)
                    current_dir = "/" + "/".join(file_path_keys)
                    current_contents = return_dir(file_contents, copied_keys) if len(file_path_keys) != 0 else file_contents
                else:
                    try:
                        file_path_keys.append(command[1])
                        current_dir = "/" + "/".join(file_path_keys)
                        current_contents = current_contents[command[1]]
                    except:
                        file_path_keys.pop()
                        current_dir = "/" + "/".join(file_path_keys)
                        print("Directory not found!")
            except:
                print("Invalid changedir command!")
        elif command[0] == "read":
            read_file(command[1])
        elif command[0] == "q":
            print("Exiting...")
        else:
            print("Invalid Command! Try again")