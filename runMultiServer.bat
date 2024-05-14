rmdir .\data\servers /S /Q
mkdir .\data\servers\server1
mkdir .\data\servers\server2
mkdir .\data\servers\velocity

robocopy ./plugins ./data/servers/server1
robocopy ./plugins ./data/servers/server2

podman compose -f docker-compose-multi-server.yml up
PAUSE