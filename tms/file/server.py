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