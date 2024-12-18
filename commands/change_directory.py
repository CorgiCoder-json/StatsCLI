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
                    new_path = copy.deepcopy(current)
                    new_view = self.return_dir(file_struct, new_path) if len(current) != 0 else file_struct
                    break
                else:
                    try:
                        new_path.append(line)
                        new_view = self.return_dir(file_struct, new_path) if len(current) != 0 else file_struct
                        break
                    except:
                        new_path.pop()
                        print("Directory not found!")
                        break
            except:
                print("Invalid changedir command!")
