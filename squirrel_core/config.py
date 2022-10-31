import os
import configparser

config = configparser.ConfigParser(allow_no_value=True, strict=True)

# The DEFAULT configs.
config.read_dict({
    "squirrel": {
        "mode": "development",
    },
    "database": {
        "host": "localhost",
        "port": "5432",
        "user": "postgresql",
        "pass": "",
        "database": "squirrel_core",
    },
})

# Try get environ variables.
env_mode = os.environ.get("SQUIRREL_MODE", "development")

# Try to read config files.
config_files = config.read([
    f"../../squirrel.ini",
    f"../../squirrel.{env_mode}.ini",
    f"../squirrel.ini",
    f"../squirrel.{env_mode}.ini",
    f"./squirrel.ini",
    f"./squirrel.{env_mode}.ini",
    f"~/.config/squirrel.ini",
    f"~/.config/squirrel.{env_mode}.ini",
    os.environ.get("SQUIRREL_CONFIG_FILE", f"{env_mode}.ini"),
])

# Combine the ENV variables.
config.read_dict({
    "squirrel": {
        "mode": env_mode,
        "config_files": config_files,
    },
})