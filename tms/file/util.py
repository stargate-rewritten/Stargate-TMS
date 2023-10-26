import shutil
import os.path as path
import os

def copyFilesInDirectoryToDirectory(source : str, destination : str):
    if not path.exists(destination):
        os.makedirs(destination)
    for fileOrDir in os.listdir(source):
        if path.isdir(path.join(source, fileOrDir)):
            copyFilesInDirectoryToDirectory(path.join(source, fileOrDir), path.join(destination, fileOrDir))
        elif path.isfile(path.join(source, fileOrDir)):
            shutil.copy(path.join(source, fileOrDir), path.join(destination, fileOrDir))
        else:
            raise NotImplementedError("Only files and directories are implemented")

def clearDirectory(directory : str):
    if not path.exists(directory):
        return
    for fileOrDir in os.listdir(directory):
        if path.isdir(path.join(directory, fileOrDir)):
            clearDirectory(path.join(directory, fileOrDir))
            os.rmdir(path.join(directory, fileOrDir))
        elif path.isfile(path.join(directory, fileOrDir)):
            os.remove(path.join(directory,fileOrDir))
        else:
            raise NotImplementedError("Only files and directories are implemented")