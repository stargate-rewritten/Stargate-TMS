import os.path as path
from tms.stage.features import FeaturesStage
from tms.stage.network import NetworkStage
from tms.stage.compat import CompatStage
from tms.config.properties import Properties

def generateCache():
    usernameMain = input("Main username (OP): ")
    usernameAlt = input("Alt username: ")

    with open("cache.properties", "w") as file:
        file.writelines(["userMain="+usernameMain+"\n", "userAlt="+usernameAlt+"\n"])

if path.exists("cache.properties"):
    msg = "Found cache, generate a new cache? (Y/N): "
    yesNo = input(msg).upper()
    while not yesNo == "N":
        if yesNo.upper() == "Y":
            generateCache()
            break
        else:
            print("Invalid input", yesNo, "expected (Y/N)")
        yesNo = input(msg).upper()
else:
    generateCache()

config = Properties("config.properties")

FeaturesStage().run()
NetworkStage().run()
CompatStage(config).run()


