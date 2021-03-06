from pathlib import Path
import os
import datetime
import uuid

import yaml


CONFIG_ENVIRONMENT_VARIABLE_NAME = "NWPC_GRAPHICS_CONFIG"


class Config(dict):
    def __init__(self, config_file_path: Path = None, **kwargs):
        super(Config).__init__(**kwargs)
        self["ncl"] = dict()
        self["config"] = dict()
        self["systems"] = dict()
        self.config_file_path = config_file_path

    @classmethod
    def load(cls, config_file: str or Path):
        with open(config_file) as f:
            config_dict = yaml.safe_load(f)
            config = Config(config_file_path=Path(config_file))
            config.update(config_dict)
            config.load_systems()
            return config

    def load_systems(self):
        systems_path = self.config_file_path.parent.joinpath(self["config"]["systems_dir"])
        if not systems_path.exists():
            raise FileNotFoundError(f"systems directory is not found.")

        for item in systems_path.iterdir():
            if item.is_dir():
                continue
            if item.suffix != ".yaml":
                continue
            with open(item) as f:
                c = yaml.safe_load(f)
                self["systems"][item.stem] = c

    def generate_run_dir(self):
        run_base_dir = os.path.expandvars(self["general"]["run_base_dir"])
        Path(run_base_dir).mkdir(parents=True, exist_ok=True)

        temp_string = str(uuid.uuid4())
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        temp_directory = f"{current_datetime}_{temp_string}"
        run_dir = Path(run_base_dir, temp_directory)
        run_dir.mkdir(parents=True, exist_ok=True)
        return run_dir


def load_config_from_env():
    if CONFIG_ENVIRONMENT_VARIABLE_NAME in os.environ:
        config = Config.load(os.environ[CONFIG_ENVIRONMENT_VARIABLE_NAME])
        return config
    return None
