import shutil
import os.path as path
import os
import subprocess


def _insert_plugins(destination_folder: str):
    for file_name in os.listdir("./plugins"):
        shutil.copy2(path.join("./plugins", file_name), destination_folder)


def init():
    if path.exists("./data/spigot"):
        shutil.rmtree("./data/spigot")
    os.makedirs("./data/spigot/plugins")
    _insert_plugins("./data/spigot/plugins")
    process = subprocess.Popen(["podman", "compose", "-f", "docker-compose-spigot.yml", "up"])
    process.wait()
