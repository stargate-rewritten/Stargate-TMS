import tkinter
from tms.config.properties import Properties
import tms.parsing.command as command
import os.path as path
from tms.directory import Directory
from tms.console import Console
from tms.kbhit import KBHit
from threading import Thread
import tms.file.util

class CompatStage():
    
    def __init__(self, config : Properties):
        self.spigotCmd = [config.getValue("java16")]
        self.spigotCmd.extend(command.parseCommand(path.join(Directory.RESOURCES.value, "runArgsSpigot.txt")))
        self.bungeeCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandBungee.txt"))
        self.tkRoot = tkinter.Tk()
        self.lineReader = KBHit()
    
    def run(self):
        print("Compatibility test.")
        print("  Moving settings and world files....")
        tms.file.util.copyFilesInDirectoryToDirectory(Directory.RESOURCE_COMPAT_SPIGOT_1.value, Directory.RUNTIME_COMPAT_SPIGOT_1.value)
        tms.file.util.copyFilesInDirectoryToDirectory(Directory.RESOURCE_COMPAT_SPIGOT_2.value, Directory.RUNTIME_COMPAT_SPIGOT_2.value)
        tms.file.util.copyFilesInDirectoryToDirectory(Directory.RESOURCE_COMPAT_BUNGEE.value, Directory.RUNTIME_COMPAT_BUNGEE.value)
        print("  Starting instances...")
        compat_console_spigot1 = Console(self.spigotCmd, tkinter.Toplevel(self.tkRoot), Directory.RUNTIME_COMPAT_SPIGOT_1.value)
        compat_console_spigot2 = Console(self.spigotCmd, tkinter.Toplevel(self.tkRoot), Directory.RUNTIME_COMPAT_SPIGOT_2.value)
        compat_console_bungee = Console(self.bungeeCmd, self.tkRoot, Directory.RUNTIME_COMPAT_BUNGEE.value, exitCmd="end")
        Thread( target=self.handleInput ).start()
        self.tkRoot.protocol("WM_DELETE_WINDOW", self._stop)
        self.tkRoot.mainloop()
        
    def _stop(self):
        self.lineReader.disable()
        self.tkRoot.destroy()
        
    def handleInput(self):
        try:
            print("  Press enter to go to the next stage")
            self.lineReader.getExit()
            self._stop()
        except EOFError:
            pass