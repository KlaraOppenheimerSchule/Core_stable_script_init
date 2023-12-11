import json
import os
from pathlib import Path

CONFIG = "core_repo_config.json"
DOCKER_COMPOSE_DOWN = "docker-compose down"


def load_data_from_config() -> dict:
    with open(CONFIG, "r") as config_json:
        config_obj: dict = json.load(config_json)
        return config_obj


def stop_containers():
    data: dict = load_data_from_config()
    os.system(DOCKER_COMPOSE_DOWN)
    os.chdir(Path().resolve().joinpath(data["core_repo_name"]))
    os.system(DOCKER_COMPOSE_DOWN)


stop_containers()
