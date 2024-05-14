rmdir /data/folia
mkdir /data/folia
robocopy ./plugins ./data/folia

podman compose -f docker-compose-folia.yml up
PAUSE