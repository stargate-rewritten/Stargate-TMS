import shutil
import os.path as path
import os
import subprocess


def _insert_plugins(destination_folder: str):
    for file_name in os.listdir("./plugins"):
        shutil.copy2(path.join("./plugins", file_name), destination_folder)


def init():
    shutil.rmtree("./data/folia")
    os.makedirs("./data/folia")
    _insert_plugins("./data/folia/plugins")
    process = subprocess.Popen(["podman", "compose", "-f", "docker-compose-folia.yml", "up"])
    process.wait()
