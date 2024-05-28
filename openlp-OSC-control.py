# from typing import Any, Dict

import OpenLPRestAPI as OLP
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer



global OpenLP

openLP = None

if __name__ == "__main__":
    authentication = OLP.OpenLPAuthentication("http://localhost:4316/","openlp","TestPassword")
    # auth_token = authentication.getAuthenticationToken()
    # print ("Received auth token:",auth_token)

    openLP = OLP.OpenLP(authentication)

    # print (f"TestResult: {openLP.controller_live_items()}")
    # print (f"TestResult: {openLP.controller_live_item()}")
    # print (f"TestResult: {openLP.controller_themes()}")
    # print (f"TestResult: {openLP.controller_theme_level()}")
    # print (f"TestResult: {openLP.controller_show(0)}")
    # print (f"TestResult: {openLP.service_progress('next')}")
    # print (f"TestResult: {openLP.controller_progress('next')}")
    # print (f"TestResult: {openLP.core_display('hide')}")
    # print (f"TestResult: {openLP.core_display('show')}")

def OpenLP_core_display(address, *args):
    openLP.core_display(args[0])

def OpenLP_controller_progress(_address, *args):
    openLP.controller_progress(args[0])

def print_handler(address, *args):
    print(f"{address}: {args}")

def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")


dispatcher = Dispatcher()
dispatcher.map("/OpenLP/core/display/*", OpenLP_core_display)
dispatcher.map("/OpenLP/controller/progress/*", OpenLP_controller_progress)
dispatcher.set_default_handler(default_handler)

ip = "127.0.0.1"
port = 1337

server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever

