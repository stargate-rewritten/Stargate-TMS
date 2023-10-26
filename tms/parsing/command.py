import re

def parseCommand(fileName):
    cmd = []
    with open(fileName) as file:
        for line in file.readlines():
            cmd.extend([string for string in re.split("[ \n]", line) if len(string) > 0])
    return cmd
