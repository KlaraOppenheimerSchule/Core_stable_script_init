import json
import os
from pathlib import Path

CONFIG = "core_repo_config.json"
DOCKER_COMPOSE_UP: str = "docker-compose up -d"
GIT_SUBMODULE_ADD: str = "git submodule add " + os.getcwd() + "/"
GIT_PULL: str = "git pull"
CLONE = "git clone "

project_path: Path = Path().resolve()


def load_data_from_config() -> dict:
    with open(CONFIG, "r") as config_json:
        config_obj: dict = json.load(config_json)
        return config_obj


def pull_changes(core_repo_name: str):
    print("build/run core")
    os.chdir(project_path.joinpath(core_repo_name))
    os.system(GIT_PULL)


def clone_repo(repo_url: str, core_repo_name: str):
    exists: bool = Path.exists(Path().resolve().joinpath(core_repo_name))
    if exists:
        return

    os.chdir(project_path)
    os.system(CLONE + repo_url)
    os.system(GIT_SUBMODULE_ADD + core_repo_name)


def run_app(core_repo_name: str):
    os.chdir(project_path.joinpath(core_repo_name))
    os.system(DOCKER_COMPOSE_UP)
    # TODO check if this should always be the case (compose)
    os.chdir(project_path)
    os.system(DOCKER_COMPOSE_UP)


def entry():
    data: dict = load_data_from_config()
    core_repo_name = data["core_repo_name"]

    clone_repo(data["core_poc_repo_url"], core_repo_name)
    pull_changes(core_repo_name)
    run_app(core_repo_name)


entry()
