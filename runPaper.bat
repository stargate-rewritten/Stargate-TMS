rmdir /data/paper
mkdir /data/paper
robocopy ./plugins ./data/paper

podman compose -f docker-compose-paper.yml up
PAUSE