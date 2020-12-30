"""A module the context around GNU stow"""


class Context():
    """Maintains options and arguments for GNU stow"""

    def __init__(self, arguments):
        self.arguments = [arg for arg in arguments if arg[0] != '-']
        self.options = [opt for opt in arguments if opt[0] == '-']
        self.executable = "stow"

    def add_option(self, val):
        """adds an option switch"""
        self.options.append(val)

    def argv(self):
        """returns the executable, options and arguments"""
        return [self.executable, *self.options, *self.arguments]
