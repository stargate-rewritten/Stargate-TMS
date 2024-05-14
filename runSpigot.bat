rmdir /data/spigot
mkdir /data/spigot
robocopy ./plugins ./data/spigot

podman run --rm -a stdin -a stdout -a stderr --tty --publish 25565:25565 -v ./data/spigot:/data/plugins localhost/spigot:latest
PAUSE