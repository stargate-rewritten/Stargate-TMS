import os.path as path
import os
from tms.console import Console
from tms.directory import Directory
import tms.parsing.command as command

paperCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandPaper.txt"))
print("Starting features instance")
console = Console()