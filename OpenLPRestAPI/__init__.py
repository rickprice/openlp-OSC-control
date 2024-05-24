class OpenLPControl:
    def __init__(self, openlpURL:Str,username:Str, password:Str):
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
    def controller_live_items(self): JSon
        pass
    def controller_live_item(self): JSon
        pass
    def controller_show(self):
        pass
    def controller_progress(self):
        pass
    def controller_themes(self): JSon
        pass
    def controller_theme(self,theme_name: Str):
        pass
    def controller_live_theme(self): JSon
        pass
    def controller_clear(self, controller_name: Str):
        pass

    def core_display(self,display_mode: Str):
        pass
    def core_plugins(self): JSon
        pass
    def core_system(self): JSon
        pass
    def core_live_image(self): Image
        pass

    def plugins_add(self,plugin: Str):
        pass
    def plugins_live(self,plugin: Str, id: Str):
        pass

    def service_items(self): JSon
        pass
    def service_show(self,id: Str):
        pass
    def service_progress(self, action: Str):
        pass
    def service_new(self):
        pass

class ControllerThemeLevel:
    def __get__(self):
        pass
    def __set__(self,themeLevel):
        pass

class ControllerCurrentTheme:
    def __get__(self):
        pass
    def __set__(self,currentTheme):
        pass
class PluginsSearchOptions:
    def __get__(self):
        pass
    def __set__(self,currentTheme):
        pass
