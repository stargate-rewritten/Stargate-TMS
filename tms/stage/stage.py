from tms.console import Console

class Stage:
    
    def __init__(self):
        self.servers = []
    
    def addConsole(self, server : Console):
        self.servers.append(server)

    