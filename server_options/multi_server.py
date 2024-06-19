import shutil
import os
import os.path as path
import subprocess


def _insert_plugins(destination_folder: str):
    for file_name in os.listdir("./plugins"):
        shutil.copy2(path.join("./plugins", file_name), destination_folder)


def init():
    shutil.rmtree("./data/servers")
    os.makedirs("./data/servers/server1/plugins")
    os.makedirs("./data/servers/server2/plugins")
    os.makedirs("./data/servers/velocity")
    _insert_plugins("./data/servers/server1/plugins")
    _insert_plugins("./data/servers/server2/plugins")
    shutil.copy2("configs/velocity.toml", "./data/servers/velocity")
    shutil.copy2("configs/forwarding.secret", "./data/servers/velocity")
    shutil.copy2("configs/spigot.yml", "./data/servers/server1")
    shutil.copy2("configs/spigot.yml", "./data/servers/server2")
    process = subprocess.Popen(["podman", "compose", "-f", "docker-compose-multi-server.yml", "up"])
    process.wait()
