from commands.base_command import Command
import copy

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
            if line[0] == '-' and len(self.subcommands) != 0:
                if line not in self.subcommands:
                    raise TypeError("Command is formatted wrong! " + line + " sub command does not exsist!")
            else:
                try:
                    copied_keys = copy.deepcopy(key_path)
                    if len(copied_keys) > 0:
                        self.update_dir(file_struct, copied_keys, line)
                    else:
                        new_struct.update({line: {}})
                    break
                except Exception as err:
                    print(err)
                    print("Invalid command input!")
        return new_struct, new_key_path