class OpenLPControl:
    def __init__(openlpURL:Str,username:Str, password:Str):
        self.authenticated = False
        self.username = username
        self.password = password
        self.authentication_token = None

    def ensure_authenticated():
        pass

    def authenticate():
        pass

    # API to talk to OpenLP: https://gitlab.com/openlp/wiki/-/wikis/Documentation/HTTP-API
    def controller_live_items_get(): JSon
        pass
    def controller_live_item_get(): JSon
        pass
    def controller_show_post():
        pass
    def controller_progress_post():
        pass
    def controller_theme_level_get(): JSon
        pass
    def controller_theme_level_post():
        pass

