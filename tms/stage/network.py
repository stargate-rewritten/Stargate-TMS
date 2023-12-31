import tms.parsing.command as command
from tms.directory import Directory
from tms.console import Console
from tms.kbhit import KBHit
import os.path as path
import tkinter
from threading import Thread

class NetworkStage():
    
    def __init__(self):
        self.paperCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandPaper.txt"))
        self.waterfallCmd = command.parseCommand(path.join(Directory.RESOURCES.value, "runCommandWaterfall.txt"))
        self.tkRoot = tkinter.Tk()
        self.lineReader = KBHit()
    
    def run(self):
        print("Network test.")
        self.consoles = {
            "paper1" : Console(self.paperCmd, tkinter.Toplevel(self.tkRoot), Directory.RUNTIME_NETWORK_PAPER_1.value),
            "paper2" : Console(self.paperCmd, tkinter.Toplevel(self.tkRoot), Directory.RUNTIME_NETWORK_PAPER_2.value),
            "waterfall" : Console(self.waterfallCmd, self.tkRoot, Directory.RUNTIME_NETWORK_WATERFALL.value, exitCmd="end"),
            }
        Thread( target=self.handleInput ).start()
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
    
    def handleInput(self):
        try:
            print("  Press enter to go to the next stage")
            self.lineReader.getExit()
            self._stop()
        except EOFError:
            pass