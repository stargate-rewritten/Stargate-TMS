import tkinter
from tms.console import Console
from tms.directory import Directory
import tms.parsing.command as command
from tms.kbhit import KBHit
import os.path as path
from threading import Thread

class FeaturesStage:
    
    def __init__(self):
        self.paperCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandPaper.txt"))
        self.tkRoot = tkinter.Tk()
        self.lineReader = KBHit()
        
    def run(self):
        print("Starting features instance...")
        features_console = Console(self.paperCmd, self.tkRoot, Directory.RUNTIME_FEATURES_PAPER.value)
        self.tkRoot.protocol("WM_DELETE_WINDOW", self._stop)
        Thread( target=self.handleInput ).start()
        self.tkRoot.mainloop()
        
    def _stop(self):
        self.lineReader.disable()
        self.tkRoot.destroy()
        
    def handleInput(self):
        try:
            print("Press enter to go to the next stage")
            self.lineReader.getExit()
            self._stop()
        except EOFError:
            pass