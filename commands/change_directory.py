from base_command import Command
import copy

class ChangeDirectory(Command):
    def __init__(self, alias, sub_commands):
        super().__init__(alias)
        self.subcommands = sub_commands
    def return_dir(self, file_dict, keys):
        if len(keys) == 1 or len(file_dict[keys[0]].keys()) == 0:
            return file_dict[keys[0]]
        next_set = file_dict[keys[0]]
        keys.pop(0)
        return self.return_dir(next_set, keys)
    def interpret(self, command_str, file_struct, current):
        new_view = {}
        new_path = current
        for line in command_str[1:]:
            try:
                if line == "<-":
                    current.pop()
                    copied_keys = copy.deepcopy(file_path_keys)
                    current_dir = "/" + "/".join(file_path_keys)
                    current_contents = self.return_dir(file_contents, copied_keys) if len(file_path_keys) != 0 else file_contents
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
