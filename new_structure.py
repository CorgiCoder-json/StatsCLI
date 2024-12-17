import copy
from commands.make_directory import MakeDirectory


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
    commands = [MakeDirectory(["makedir", "mkdir", "mk"], [])]
    user_in = ""
    while True:
        user_in = input("Enter command: ").split()
        if user_in[0] == "q":
            break
        run_command(commands, user_in, file_sys, file_key_path)
        print(file_sys)