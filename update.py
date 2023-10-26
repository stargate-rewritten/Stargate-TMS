import subprocess
import os.path as path
import os
import requests
import tms.parsing.command as command
from tms.directory import Directory
import tms.file.server
import tms.file.util

PAPER_DOWNLOAD_URL = "https://api.papermc.io/v2/projects/paper/versions/1.20.2/builds/246/downloads/paper-1.20.2-246.jar"

tms.file.util.clearDirectory(Directory.COMPILE_PAPER.value)
if not path.exists(Directory.COMPILE_PAPER.value):
    os.makedirs(Directory.COMPILE_PAPER.value)

print("Downloading paper...")
with requests.get(PAPER_DOWNLOAD_URL, allow_redirects=True) as request:
    with open(path.join(Directory.COMPILE_PAPER.value, "server.jar"), "wb") as file:
        file.write(request.content)

print("Downloading server cache")
updateCmdPaper = command.parseCommand(path.join(Directory.RESOURCES.value, "updateCommandPaper.txt"))
processPaper = subprocess.Popen(updateCmdPaper, cwd=Directory.COMPILE_PAPER.value)
processPaper.wait()

print("Copying server cache")
tms.file.server.updatePaper(Directory.RUNTIME_FEATURES_PAPER.value)
tms.file.server.updatePaper(Directory.RUNTIME_NETWORK_PAPER_1.value)
tms.file.server.updatePaper(Directory.RUNTIME_NETWORK_PAPER_2.value)