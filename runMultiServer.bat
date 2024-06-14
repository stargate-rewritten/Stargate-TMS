rmdir .\data\servers /S /Q
mkdir .\data\servers\server1\plugins
mkdir .\data\servers\server2\plugins
mkdir .\data\servers\velocity

robocopy ./plugins ./data/servers/server1/plugins
robocopy ./plugins ./data/servers/server2/plugins
copy velocity.toml .\data\servers\velocity\velocity.toml /a
copy forwarding.secret .\data\servers\velocity\forwarding.secret /a

podman compose -f docker-compose-multi-server.yml up
PAUSE