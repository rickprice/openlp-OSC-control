from typing import Any, Dict
import requests
# import json

# from requests.models import auth

class OpenLPAuthentication:
    def __init__(self, openLP_base_url: str, username: str, password: str) -> None:
        self.openLP_base_url = openLP_base_url
        self.username = username
        self.password = password
        self.authentication_token = None

    def getAuthenticationToken(self) -> str:
        if self.authentication_token is None:
            auth_data = {"username":self.username,"password":self.password}
            r = requests.post(self.makeURL("core/login"), json = auth_data)
            r.raise_for_status()
            self.authentication_token = r.json()["token"]
        return self.authentication_token

    def makeURL(self, path: str) -> str:
        return self.openLP_base_url + "api/v2/"+ path

    def get(self,path: str) -> Any:
        headers = {"Authorization" : self.getAuthenticationToken()}
        r = requests.get(self.makeURL(path),headers = headers)
        r.raise_for_status()
        return r.json()

    def post(self,path: str, payload: Any ) -> None:
        headers = {"Authorization" : self.getAuthenticationToken()}
        r = requests.post(self.makeURL(path),json=payload, headers = headers)
        r.raise_for_status()
        # return r.json()


class OpenLP:
    def __init__( self, authentication: OpenLPAuthentication):
        self.authentication = authentication

        self.controller_themeLevel = ControllerThemeLevel()
        self.controller_currentTheme = ControllerCurrentTheme()

        self.plugins_search_options = PluginsSearchOptions()


    # API to talk to OpenLP: https://gitlab.com/openlp/wiki/-/wikis/Documentation/HTTP-API
    def controller_live_items(self) -> Any:
        return self.authentication.get("controller/live-items")

    def controller_live_item(self) -> Any:
        return self.authentication.get("controller/live-item")

    def controller_show(self, id: str):
        payload = {"id":id}
        return self.authentication.post("controller/show",payload)

    def controller_progress(self, action: str):
        payload = {"action": action}
        return self.authentication.post("controller/progress",payload)

    def controller_theme_level(self) -> Any:
        return self.authentication.get("controller/theme-level")

    def controller_themes(self) -> Any:
        return self.authentication.get("controller/themes")

    def controller_theme(self, theme_name: str):
        return self.authentication.get(f"controller/themes/{theme_name}")

    def controller_live_theme(self) -> Any:
        return self.authentication.get("controller/live-theme")

    def controller_clear(self, controller_name: str):
        return self.authentication.post("controller/clear/{controller_name}", None)

    def core_display(self, display_mode: str):
        payload = {"display":display_mode}
        return self.authentication.post("core/display",payload)

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
        payload = {"action": action}
        return self.authentication.post("service/progress",payload)

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
    authentication = OpenLPAuthentication("http://localhost:4316/","openlp","TestPassword")
    # auth_token = authentication.getAuthenticationToken()
    # print ("Received auth token:",auth_token)

    openLP = OpenLP(authentication)

    # print (f"TestResult: {openLP.controller_live_items()}")
    # print (f"TestResult: {openLP.controller_live_item()}")
    # print (f"TestResult: {openLP.controller_themes()}")
    # print (f"TestResult: {openLP.controller_theme_level()}")
    # print (f"TestResult: {openLP.controller_show(0)}")
    # print (f"TestResult: {openLP.service_progress('next')}")
    # print (f"TestResult: {openLP.controller_progress('next')}")
    print (f"TestResult: {openLP.core_display('show')}")

