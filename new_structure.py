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
    def interpret(self, command_str, file_struct, current):
        new_struct = file_struct
        new_current = current
        if command_str[0] not in self.alias:
            raise ValueError("Command is not here!")
        for line in command_str[1:]:
            if line[0] == '-':
                if line not in self.subcommands:
                    raise TypeError("Command is formatted wrong! " + line + " sub command does not exsist!")
            else:
                try:
                    copied_keys = copy.deepcopy(file_path_keys)
                    if len(file_path_keys) > 0:
                        update_dir(file_contents, copied_keys, command[1])
                    else:
                        file_contents.update({command[1]: {}})
                except Exception as err:
                    print(err)
                    print("Invalid command input!")
            
        return new_struct, new_current

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