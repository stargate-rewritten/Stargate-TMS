rmdir /data/folia
mkdir /data/folia
robocopy ./plugins ./data/folia

podman run --rm -a stdin -a stdout -a stderr --tty --publish 25565:25565 -v ./data/folia:/data/plugins localhost/folia:latest
PAUSE