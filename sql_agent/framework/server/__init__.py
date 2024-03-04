from abc import ABC, abstractmethod

from sql_agent.setting import System, env_settings
from sql_agent.server.api import API

system = System()


class WebFrameworkServer(ABC):
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.app = self.create_app()
        self.settings = env_settings
        self.system = system
        self._api = self.init_api()
        self.add_routes(self.app)

    @abstractmethod
    def create_app(self):
        pass

    @abstractmethod
    def run_server(self):
        pass

    @abstractmethod
    def add_routes(self, app):
        pass

    def init_api(self):
        return self.system.get_module(API)
