class Command:
    def __init__(self, alias):
        self.alias = alias
    def interpret(self, command_str, file_struct, current):
        pass
    def __str__(self):
        return (f"This is a base command.\n This is just a placeholder.\n If you are seeing this," 
        +f"then this command has not been fully implemented")