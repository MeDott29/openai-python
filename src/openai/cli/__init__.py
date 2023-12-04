from ._cli import main as main
from .cheat_sheet import main as cheat_sheet_main

class CLI:
    def add_command(self, name, function):
        pass  # this is just a placeholder for demonstration purposes

# Assuming we need to instantiate the CLI and add the command
cli = CLI()
cli.add_command("cheat_sheet", cheat_sheet_main)

