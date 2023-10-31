import tkinter
from tms.config.properties import Properties
import tms.parsing.command as command
import os.path as path
from tms.directory import Directory
from tms.console import Console
from tms.kbhit import KBHit
from threading import Thread
import tms.file.server

class CompatStage():
    
    def __init__(self, config : Properties):
        self.spigotCmd = [config.getValue("java16")]
        self.spigotCmd.extend(command.parseCommand(path.join(Directory.RESOURCES.value, "runArgsSpigot.txt")))
        self.bungeeCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandBungee.txt"))

        self.lineReader = KBHit()
    
    def run(self):
        print("Compatibility test.")
        print("  Refreshing settings and world files....")
        tms.file.server.refreshDataServer(Directory.RESOURCE_COMPAT_SPIGOT_1.value, Directory.RUNTIME_COMPAT_SPIGOT_1.value)
        tms.file.server.refreshDataServer(Directory.RESOURCE_COMPAT_SPIGOT_2.value, Directory.RUNTIME_COMPAT_SPIGOT_2.value)
        Thread( target=self.startInstances ).start()
        self.handleInput()
    
    def startInstances(self):
        print("  Starting instances...")
        self.tkRoot = tkinter.Tk()
        self.consoles = {
            "spigot1" : Console(self.spigotCmd, tkinter.Toplevel(self.tkRoot), Directory.RUNTIME_COMPAT_SPIGOT_1.value),
            "spigot2" : Console(self.spigotCmd, tkinter.Toplevel(self.tkRoot), Directory.RUNTIME_COMPAT_SPIGOT_2.value),
            "bungee" : Console(self.bungeeCmd, self.tkRoot, Directory.RUNTIME_COMPAT_BUNGEE.value, exitCmd="end")
            }
        
        self.tkRoot.protocol("WM_DELETE_WINDOW", self._stop)
        self.tkRoot.mainloop()
    
    def _stop(self):
        self.lineReader.disable()
        threads = []
        for key in self.consoles:
            thread = Thread(target=self.consoles[key].stopProcess)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        self.tkRoot.destroy()
        
    def restartInstances(self):
        threads = []
        for key in self.consoles:
            thread = Thread(target=self.consoles[key].restart)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
    def handleInput(self):
        try:
            print("  Press enter to restart the server")
            self.lineReader.getExit()
            self.restartInstances()
            print("  Press enter to exit this stage of testing")
            self.lineReader.getExit()
            self._stop()
        except EOFError:
            pass