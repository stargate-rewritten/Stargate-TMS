import tms.file.util as util
import os.path as path
import shutil
from tms.directory import Directory

def updatePaper(destination : str):
    source = Directory.COMPILE_PAPER.value
    dirsToCopy = ["cache", "libraries", "versions"]
    for directory in dirsToCopy:
        util.copyFilesInDirectoryToDirectory(path.join(source, directory), path.join(destination, directory))
    
    shutil.copy(path.join(source, "server.jar"), path.join(destination, "server.jar"))
    

def refreshDataServer(source : str, destination : str):
    util.clearDirectory(path.join(destination, "world"))
    util.clearDirectory(path.join(destination, "world_nether"))
    util.clearDirectory(path.join(destination, "world_end"))
    util.clearDirectory(path.join(destination, "plugins"))
    util.clearDirectory(path.join(destination, "logs"))
    util.copyFilesInDirectoryToDirectory(source, destination)