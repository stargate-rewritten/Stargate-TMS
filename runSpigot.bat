rmdir /data/spigot
mkdir /data/spigot
robocopy ./plugins ./data/spigot

podman compose -f docker-compose-spigot.yml up
PAUSE