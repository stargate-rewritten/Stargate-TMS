import subprocess
import os.path as path
import os
import requests
import shutil
import tms.parsing.command as command
from tms.directory import Directory
import tms.file.server
import tms.file.util
from tms.config.properties import Properties

config = Properties("config.properties")

tms.file.util.clearDirectory(Directory.COMPILE.value)
if not path.exists(Directory.COMPILE_PAPER.value):
    os.makedirs(Directory.COMPILE_PAPER.value)

print("Downloading paper...")
with requests.get(config.getValue("paper"), allow_redirects=True) as request:
    with open(path.join(Directory.COMPILE_PAPER.value, "server.jar"), "wb") as file:
        file.write(request.content)

print("Downloading paper server cache...")
updateCmdPaper = command.parseCommand(path.join(Directory.RESOURCES.value, "updateCommandPaper.txt"))
processPaper = subprocess.Popen(updateCmdPaper, cwd=Directory.COMPILE_PAPER.value)
processPaper.wait()

print("Copying paper server cache...")
tms.file.server.updatePaper(Directory.RUNTIME_FEATURES_PAPER.value)
tms.file.server.updatePaper(Directory.RUNTIME_NETWORK_PAPER_1.value)
tms.file.server.updatePaper(Directory.RUNTIME_NETWORK_PAPER_2.value)

if not path.exists(Directory.COMPILE_SPIGOT.value):
    os.makedirs(Directory.COMPILE_SPIGOT.value)
print("Downloading spigot...")
with requests.get(config.getValue("spigot"), allow_redirects=True) as request:
    with open(path.join(Directory.COMPILE_SPIGOT.value, "server.jar"), "wb") as file:
        file.write(request.content)

print("Copying spigot to instances...")
spigotDestinations = [Directory.RUNTIME_COMPAT_SPIGOT_1.value, Directory.RUNTIME_COMPAT_SPIGOT_2.value]
for spigotDestination in spigotDestinations:
    if not path.exists(spigotDestination):
        os.makedirs(spigotDestination)
    shutil.copy(path.join(Directory.COMPILE_SPIGOT.value, "server.jar"), path.join(spigotDestination,"server.jar"))

if not path.exists(Directory.COMPILE_WATERFALL.value):
    os.makedirs(Directory.COMPILE_WATERFALL.value)
print("Downloading waterfall...")
with requests.get(config.getValue("waterfall"), allow_redirects=True) as request:
    with open(path.join(Directory.COMPILE_WATERFALL.value, "proxy.jar"), "wb") as file:
        file.write(request.content)
print("Copying waterfall")
shutil.copy(path.join(Directory.COMPILE_WATERFALL.value, "proxy.jar"), path.join(Directory.RUNTIME_NETWORK_WATERFALL.value, "proxy.jar"))
print("Update finished!")