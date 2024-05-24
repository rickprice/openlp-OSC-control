from typing import Any
import requests
from requests.models import auth


class OpenLPAuthentication:
    def __init__(self, OpenLP_url: str, username: str, password: str) -> None:
        self.openLP_url = OpenLP_url
        self.username = username
        self.password = password
        self.authenticated = False
        self.authentication_token = None

    def getAuthenticationToken(self) -> str:
        # FIX: Uhh, need to get a token
        return "+++BrokenToken+++"


class OpenLPControl:
    def __init__( self, authentication: OpenLPAuthentication):
        self.authentication = authentication

        self.controller_themeLevel = ControllerThemeLevel()
        self.controller_currentTheme = ControllerCurrentTheme()

        self.plugins_search_options = PluginsSearchOptions()


    def ensure_authenticated(self):
        pass

    def authenticate(self):
        pass

    # API to talk to OpenLP: https://gitlab.com/openlp/wiki/-/wikis/Documentation/HTTP-API
    def controller_live_items(self) -> Any:
        pass

    def controller_live_item(self) -> Any:
        pass

    def controller_show(self):
        pass

    def controller_progress(self):
        pass

    def controller_themes(self) -> Any:
        pass

    def controller_theme(self, theme_name: str):
        pass

    def controller_live_theme(self) -> Any:
        pass

    def controller_clear(self, controller_name: str):
        pass

    def core_display(self, display_mode: str):
        pass

    def core_plugins(self) -> Any:
        pass

    def core_system(self) -> Any:
        pass

    def core_live_image(self) -> Any:
        pass

    def plugins_add(self, plugin: str):
        pass

    def plugins_live(self, plugin: str, id: str):
        pass

    def service_items(self) -> Any:
        pass

    def service_show(self, id: str):
        pass

    def service_progress(self, action: str):
        pass

    def service_new(self):
        pass


class ControllerThemeLevel:
    def __get__(self):
        pass

    def __set__(self, themeLevel):
        pass


class ControllerCurrentTheme:
    def __get__(self):
        pass

    def __set__(self, currentTheme):
        pass


class PluginsSearchOptions:
    def __get__(self):
        pass

    def __set__(self, currentTheme: str):
        pass
