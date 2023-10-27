import os.path as path
import os
from tms.console import Console
from tms.directory import Directory
import tms.parsing.command as command
import tkinter

paperCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandPaper.txt"))
print("Starting features instance")
tkRoot = tkinter.Tk()
features_console = Console(paperCmd, tkRoot, Directory.RUNTIME_FEATURES_PAPER.value)
tkRoot.mainloop()


print("Starting network instances")
network_console_paper1 = Console(paperCmd, tkRoot, Directory.RUNTIME_NETWORK_PAPER_1.value)
network_console_paper2 = Console(paperCmd, tkRoot, Directory.RUNTIME_NETWORK_PAPER_2.value)
tkRoot.mainloop()