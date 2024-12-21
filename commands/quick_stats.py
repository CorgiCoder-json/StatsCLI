from base_command import Command
import numpy as np
import copy

class StatsObject:
    def __init__(self):
        self.mean = 0
        self.median = 0
        self.pop_std = 0
        self.sam_std = 0
        self.min = 0
        self.max = 0
        self.q1 = 0
        self.q3 = 0
    def apply(self, data):
        try:
            self.mean = np.mean(data)
            self.median = np.median(data)
            self.pop_std = np.std(data)
            self.sam_std = np.std(data, ddof=1)
            self.min = min(data)
            self.max = max(data)
            self.q1 = np.quantile(data, 1)
            self.q3 = np.quantile(data, 3)
        except:
            print("Data is not of type float, double or int!")
    def __str__(self):
        return f"Done!"

class QuickStats(Command):
    def __init__(self, alias, sub_commands):
        super().__init__(alias)
        self.subcommands = sub_commands
    def interpret(self, command_str, file_struct, current):
        if command_str[0] not in self.alias:
            raise ValueError("Command is not here!")
        if len(command_str[1:]) == 0:
            try:
                view = self.get_current_view(file_struct, current) if len(current) != 0 else file_struct
                print(list(view.keys()))
            except:
                print("Something went wrong!")
        for line in command_str[1:]:
            if line[0] == '-' and len(self.subcommands) != 0:
                if line not in self.subcommands:
                    raise TypeError("Command is formatted wrong! " + line + " sub command does not exsist!")
            try:
                view = self.get_current_view(file_struct, current) if len(current) != 0 else file_struct
                print("Inside List Dir!!!")
                print(list(view.keys()))
            except:
                print("Something went wrong!")
        return file_struct, current