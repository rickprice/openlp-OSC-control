from typing import Any


class OpenLPControl:
    def __init__(self, openlpURL: str, username: str, password: str):
        self.controller_themeLevel = ControllerThemeLevel()
        self.controller_currentTheme = ControllerCurrentTheme()

        self.plugins_search_options = PluginsSearchOptions()

        # Authentication Bits
        self.authenticated = False
        self.username = username
        self.password = password
        self.authentication_token = None

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
