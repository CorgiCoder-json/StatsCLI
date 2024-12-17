import copy

class Command:
    def __init__(self, alias):
        self.alias = alias
    def interpret(self, command_str, file_struct, current):
        pass
    def __str__(self):
        return (f"This is a base command.\n This is just a placeholder.\n If you are seeing this, 
        then this command has not been fully implemented")

class MakeDirectory(Command):
    def __init__(self, alias, sub_commands):
        super().__init__(alias)
        self.subcommands = sub_commands
    def update_dir(self, file_dict, keys, new_dir):
        if len(keys) == 1 or len(file_dict[keys[0]].keys()) == 0:
            file_dict[keys[0]].update({new_dir: {}})
            return 0
        next_set = file_dict[keys[0]]
        keys.pop(0)
        return self.update_dir(next_set, keys, new_dir)
    def interpret(self, command_str, file_struct, key_path):
        new_struct = file_struct
        new_key_path = key_path
        if command_str[0] not in self.alias:
            raise ValueError("Command is not here!")
        for line in command_str[1:]:
            if line[0] == '-':
                if line not in self.subcommands:
                    raise TypeError("Command is formatted wrong! " + line + " sub command does not exsist!")
            else:
                try:
                    copied_keys = copy.deepcopy(key_path)
                    if len(copied_keys) > 0:
                        self.update_dir(file_struct, copied_keys, line)
                    else:
                        file_struct.update({line: {}})
                except Exception as err:
                    print(err)
                    print("Invalid command input!")
        return new_struct, new_key_path

def run_command(commands_list, command_str):
    new_file_struct = {}
    new_current_dir = {}
    for command in commands_list:
        try:
            new_file_struct, new_current_dir = command.interpret(command_str, file_struct, current_direct)
        except ValueError as err:
            continue
        except TypeError as err:
            print(err)
    return new_file_struct, new_current_dir