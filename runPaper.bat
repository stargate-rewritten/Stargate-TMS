rmdir /data/paper
mkdir /data/paper
robocopy ./plugins ./data/paper

podman run --rm -a stdin -a stdout -a stderr --tty --publish 25565:25565 -v ./data/paper:/data/plugins localhost/paper:latest
PAUSE