import os.path as path
import os
from tms.console import Console
from tms.directory import Directory
import tms.parsing.command as command
import tkinter
from tms.config.properties import Properties

config = Properties("config.properties")
paperCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandPaper.txt"))
spigotCmd = [config.getValue("java16")]
spigotCmd.extend(command.parseCommand(path.join(Directory.RESOURCES.value, "runArgsSpigot.txt")))


command.parseCommand(path.join(Directory.RESOURCES.value, ""))
waterfallCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandWaterfall.txt"))
bungeeCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandBungee.txt"))
print("Starting features instance...")
tkRoot = tkinter.Tk()
features_console = Console(paperCmd, tkRoot, Directory.RUNTIME_FEATURES_PAPER.value)
tkRoot.mainloop()


print("Starting network instances...")
tkRoot = tkinter.Tk()
network_console_paper1 = Console(paperCmd, tkRoot, Directory.RUNTIME_NETWORK_PAPER_1.value)
network_console_paper2 = Console(paperCmd, tkinter.Toplevel(tkRoot), Directory.RUNTIME_NETWORK_PAPER_2.value)
network_console_waterfall = Console(waterfallCmd, tkinter.Toplevel(tkRoot), Directory.RUNTIME_NETWORK_WATERFALL.value)
tkRoot.mainloop()

print("Starting compat instances...")
tkRoot = tkinter.Tk()
compat_console_spigot1 = Console(spigotCmd, tkRoot, Directory.RUNTIME_COMPAT_SPIGOT_1.value)
compat_console_spigot2 = Console(spigotCmd, tkinter.Toplevel(tkRoot), Directory.RUNTIME_COMPAT_SPIGOT_2.value)
compat_console_bungee = Console(bungeeCmd, tkinter.Toplevel(tkRoot), Directory.RUNTIME_COMPAT_BUNGEE.value)
tkRoot.mainloop()