from typing import Any
import requests
import json

# from requests.models import auth


class OpenLPAuthentication:
    def __init__(self, openLP_base_url: str, username: str, password: str) -> None:
        self.openLP_base_url = openLP_base_url
        self.username = username
        self.password = password
        self.authentication_token = None

    def getAuthenticationToken(self) -> str:
        if self.authentication_token is not None:
            return self.authentication_token
        else:
            url = self.openLP_base_url + "api/v2/core/login"
            # url = self.openLP_base_url + "api/v2/controller/themes"
            print("Frederick URL: ",url)
            auth_data = {"username":self.username,"password":self.password}
            # r = requests.post(url, data = json.dumps(auth_data))
            r = requests.post(url, json = auth_data)
            # r = requests.get(url)
            if r.status_code == requests.codes.ok:
                print ("returned data:", r.text)
                # self.authentication_token = r.json()[0]["authentication_token"]
            else:
                print("Got return:",r.status_code,r.text)
            return self.authentication_token

    def getOpenLPBaseURL(self)->str:
        return self.openLP_base_url


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


if __name__ == "__main__":
    # authentication = OpenLPAuthentication("http://192.168.50.165:4316/","openlp","TestPassword")
    authentication = OpenLPAuthentication("http://localhost:4316/","openlp","TestPassword")
    auth_token = authentication.getAuthenticationToken()

