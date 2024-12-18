from commands.base_command import Command
import copy

class ChangeDirectory(Command):
    def __init__(self, alias, sub_commands):
        super().__init__(alias)
        self.subcommands = sub_commands

    def get_current_view(self, file_dict, keys):
        if len(file_dict[keys[0]].keys()) == 0 or len(keys) == 1:
            return file_dict[keys[0]]
        next_set = file_dict[keys[0]]
        keys.pop(0)
        return self.return_dir(next_set, keys)
    
    def interpret(self, command_str, file_struct, current):
        new_path = current
        for line in command_str[1:]:
            try:
                if line == "<-":
                    current.pop()
                    new_path = copy.deepcopy(current)
                    break
                else:
                    try:
                        new_path.append(line)
                        view = self.get_current_view(file_struct, current)
                        break
                    except:
                        new_path.pop()
                        print("Directory not found!")
                        break
            except:
                print("Invalid changedir command!")
        return file_struct, new_path
