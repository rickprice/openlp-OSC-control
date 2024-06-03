#! /usr/bin/env python3

# from typing import Any, Dict

from OpenLPOSCControl import OpenLPRestAPI as OLP
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer


global openLP

def main():
    global openLP

    print("Starting up OpenLP OSC -> REST converter")

    authentication = OLP.OpenLPAuthentication("http://localhost:4316/","openlp","TestPassword")
    # auth_token = authentication.getAuthenticationToken()
    # print ("Received auth token:",auth_token)

    openLP = OLP.OpenLP(authentication)

    dispatcher = Dispatcher()
    dispatcher.map("/OpenLP/core/display", OpenLP_core_display)
    dispatcher.map("/OpenLP/controller/progress", OpenLP_controller_progress)
    dispatcher.set_default_handler(default_handler)

    ip = "127.0.0.1"
    port = 1337

    server = BlockingOSCUDPServer((ip, port), dispatcher)
    server.serve_forever()  # Blocks forever


    # print (f"TestResult: {openLP.controller_live_items()}")
    # print (f"TestResult: {openLP.controller_live_item()}")
    # print (f"TestResult: {openLP.controller_themes()}")
    # print (f"TestResult: {openLP.controller_theme_level()}")
    # print (f"TestResult: {openLP.controller_show(0)}")
    # print (f"TestResult: {openLP.service_progress('next')}")
    # print (f"TestResult: {openLP.controller_progress('next')}")
    # print (f"TestResult: {openLP.core_display('hide')}")
    # print (f"TestResult: {openLP.core_display('show')}")

def OpenLP_core_display(_address, *args):
    global openLP
    openLP.core_display(args[0])

def OpenLP_controller_progress(_address, *args):
    global openLP
    openLP.controller_progress(args[0])

def print_handler(address, *args):
    global openLP
    print(f"{address}: {args}")

def default_handler(address, *args):
    global openLP
    print(f"DEFAULT (unhandled): {address}: {args}")



if __name__ == "__main__":
    main()