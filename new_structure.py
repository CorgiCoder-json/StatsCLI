import copy
from commands.make_directory import MakeDirectory
from commands.change_directory import ChangeDirectory

def run_command(commands_list, command_str, file_struct, current):
    new_file_struct = {}
    new_current_dir = current
    for command in commands_list:
        try:
            new_file_struct, new_key_path = command.interpret(command_str, file_struct, current)
        except ValueError as err:
            continue
        except TypeError as err:
            print(err)
    return new_file_struct, new_current_dir

if __name__ == "__main__":
    file_sys = {}
    file_key_path = []
    commands = [MakeDirectory(["makedir", "mkdir", "mk"], []), ChangeDirectory(["changedir", "cd"], [])]
    user_in = ""
    struct = file_sys
    path = file_key_path
    while True:
        print(struct)
        print(path)
        user_in = input("Enter command: ").split()
        if user_in[0] == "q":
            break
        struct, path = run_command(commands, user_in, file_sys, file_key_path)
        print(struct)
        print(path)
    