
podman build ./docker/maven --tag localhost/plugins:latest
rmdir "plugins" /S /Q
mkdir "plugins"
podman run --rm -v plugins:/plugins localhost/plugins:latest
PAUSE