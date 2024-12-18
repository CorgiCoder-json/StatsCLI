from commands.base_command import Command
import copy

class ListDirectory(Command):
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
        new_path = copy.deepcopy(current)
        if len(command_str[1:]) == 0:
            try:
                view = self.get_current_view(file_struct, new_path)
                print("Inside List Dir!!!")
                print(list(view.keys()))
            except:
                print("Something went wrong!")
        for line in command_str[1:]:
            try:
                view = self.get_current_view(file_struct, new_path)
                print("Inside List Dir!!!")
                print(list(view.keys()))
            except:
                print("Something went wrong!")
        return file_struct, new_path
