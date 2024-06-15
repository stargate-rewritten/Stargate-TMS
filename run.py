import argparse
import server_options.multi_server
import server_options.paper_server
import server_options.spigot_server
import server_options.folia_server
import compile_plugins

parser = argparse.ArgumentParser(description="Run one or multiple minecraft servers")
parser.add_argument("--server-option", help="Choose what type of server(s) to run", type=str,
                    choices=["multi-server", "paper-server", "spigot-server", "folia-server"])
parser.add_argument("--compile-plugins", help="Recompile all plugins")
args = parser.parse_args()

if not(any(vars(args).values())):
    print("No argument specified, use -h for information about arguments")

if args.compile_plugins:
    compile_plugins.init()

server_option = args.server_option
if server_option is not None:
    if server_option == "multi-server":
        server_options.multi_server.init()

    elif server_option == "paper-server":
        server_options.paper_server.init()

    elif server_option == "spigot-server":
        server_options.spigot_server.init()

    elif server_option == "folia-server":
        server_options.folia_server.init()
    else:
        raise RuntimeError("Illegal state")
