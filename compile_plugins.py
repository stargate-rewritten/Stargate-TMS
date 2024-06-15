import subprocess


def init():
    subprocess.run(["podman", "build", "./docker/maven", "--tag", "localhost/plugins:latest"])
    subprocess.run(["podman", "run", "--rm", "-v", "plugins:/plugins", "localhost/plugins:latest"])
    print()
    print("Finished compiling plugins!")
