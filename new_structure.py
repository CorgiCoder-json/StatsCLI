import copy
from commands.make_directory import MakeDirectory
from commands.change_directory import ChangeDirectory
from commands.list_directory import ListDirectory
from commands.add_data import AddData

def return_dir(self, file_dict, keys):
        if len(keys) == 1 or len(file_dict[keys[0]].keys()) == 0:
            return file_dict[keys[0]]
        next_set = file_dict[keys[0]]
        keys.pop(0)
        return self.return_dir(next_set, keys)

def run_command(commands_list, command_str, file_struct, current):
    new_file_struct = {}
    new_current_dir = current
    for command in commands_list:
        try:
            new_file_struct, new_current_dir = command.interpret(command_str, file_struct, current)
            break
        except ValueError as err:
            continue
        except TypeError as err:
            print(err)
    return new_file_struct, new_current_dir

if __name__ == "__main__":
    file_sys = {}
    file_key_path = []
    commands = [MakeDirectory(["makedir", "mkdir", "mk"], []), ChangeDirectory(["changedir", "cd"], []), 
                ListDirectory(["listdir", "ls"], []), AddData(["add", "apply"], ["-i", "-f", "-b", "-s"])]
    user_in = ""
    struct = file_sys
    path = file_key_path
    while True:
        user_in = input("Enter command: ").split()
        if user_in[0] == "q":
            break
        struct, path = run_command(commands, user_in, file_sys, file_key_path)
        file_sys = struct
        file_key_path = path
        print(file_sys)
        print(file_key_path)
    