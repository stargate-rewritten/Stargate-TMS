podman build ./docker/maven --tag localhost/plugins:latest
podman run --rm -v plugins:/plugins localhost/plugins:latest
PAUSE