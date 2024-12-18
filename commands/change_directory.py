from commands.base_command import Command
import copy

class ChangeDirectory(Command):
    def __init__(self, alias, sub_commands):
        super().__init__(alias)
        self.subcommands = sub_commands
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
                        break
                    except:
                        new_path.pop()
                        print("Directory not found!")
                        break
            except:
                print("Invalid changedir command!")
        return file_struct, new_path
