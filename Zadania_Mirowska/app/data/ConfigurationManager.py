import json
import os
from pathlib import Path

from app.model.ApplicationData import ApplicationData

CONFIG_PATH = "config.json"


class ConfigurationJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ApplicationData):
            return o.as_dict()
        if isinstance(o, Path):
            return str(o)
        else:
            return json.JSONEncoder.default(self, o)


class Configuration:
    def __init__(self, config_path):
        self.config_path = config_path
        self.applications_list = []

    def save(self):
        application_dict = {
            "applications_list": self.applications_list
        }
        with open(self.config_path, 'w') as f:
            json.dump(application_dict, f, cls=ConfigurationJSONEncoder)

    def load(self):
        config_json = {}
        if not os.path.exists(self.config_path):
            return

        with open(self.config_path, 'r') as f:
            config_json = json.load(f)

        if not bool(config_json):
            return

        self.applications_list.clear()
        for app in config_json['applications_list']:
            self.applications_list.append(ApplicationData.from_dict(app))


class ConfigurationManager:
    configuration = Configuration(CONFIG_PATH)

    @staticmethod
    def get_configuration():
        return ConfigurationManager.configuration

    @staticmethod
    def save_configuration():
        ConfigurationManager.configuration.save()

    @staticmethod
    def load_configuration():
        ConfigurationManager.configuration.load()
