from enum import Enum
import os.path as path

class Directory(Enum):
    WORKSPACE = "workspace"
    RESOURCES = "resources"
    RESOURCE_COMPAT = path.join(RESOURCES, "compat")
    RESOURCE_COMPAT_SPIGOT_1 = path.join(RESOURCE_COMPAT, "spigot1")
    RESOURCE_COMPAT_SPIGOT_2 = path.join(RESOURCE_COMPAT, "spigot2")
    RESOURCE_COMPAT_BUNGEE = path.join(RESOURCE_COMPAT, "bungee")
    COMPILE = path.join(WORKSPACE, "resources")
    COMPILE_PAPER = path.join(COMPILE, "paper")
    COMPILE_SPIGOT = path.join(COMPILE, "spigot")
    COMPILE_WATERFALL = path.join(COMPILE, "waterfall")
    COMPILE_BUNGEE = path.join(COMPILE, "bungee")
    RUNTIMES = path.join(WORKSPACE, "runtimes")
    RUNTIME_COMPAT = path.join(RUNTIMES, "compat")
    RUNTIME_COMPAT_INSTANCES = path.join(RUNTIME_COMPAT, "instances")
    RUNTIME_COMPAT_SPIGOT_1 = path.join(RUNTIME_COMPAT_INSTANCES, "spigot1")
    RUNTIME_COMPAT_SPIGOT_2 = path.join(RUNTIME_COMPAT_INSTANCES, "spigot2")
    RUNTIME_COMPAT_BUNGEE = path.join(RUNTIME_COMPAT,"proxy","bungee")
    RUNTIME_FEATURES_PAPER = path.join(RUNTIMES, "features", "instances", "paper")
    RUNTIME_NETWORK = path.join(RUNTIMES, "network")
    RUNTIME_NETWORK_INSTANCES = path.join(RUNTIME_NETWORK, "instances")
    RUNTIME_NETWORK_PAPER_1 = path.join(RUNTIME_NETWORK_INSTANCES, "paper1")
    RUNTIME_NETWORK_PAPER_2 = path.join(RUNTIME_NETWORK_INSTANCES, "paper2")
    RUNTIME_NETWORK_PROXY = path.join(RUNTIME_NETWORK, "proxy")
    RUNTIME_NETWORK_WATERFALL = path.join(RUNTIME_NETWORK_PROXY, "waterfall")
    RUNTIME_NETWORK_VELOCITY = path.join(RUNTIME_NETWORK_PROXY, "velocity")
    RUNTIME_MODULES = path.join(RUNTIMES, "modules")
    RUNTIME_MODULES_SGI = path.join(RUNTIME_MODULES, "sgi")
    RUNTIME_MODULES_SGM = path.join(RUNTIME_MODULES, "sgm")
    RUNTIME_MODULES_SGC = path.join(RUNTIME_MODULES, "sgc")