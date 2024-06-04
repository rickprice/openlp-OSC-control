#! /usr/bin/env python3

# from typing import Any, Dict

from OpenLPOSCControl import OpenLPRestAPI as OLP
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse


global openLP

def main():
    global openLP

    parser = argparse.ArgumentParser()
    parser.add_argument('--OpenLP_REST_URL', help='URL for OpenLP REST API', default = "http://localhost:4316/")
    parser.add_argument('--ListenIP', help='IP address to listen on', default = "127.0.0.1")
    parser.add_argument('--ListenPort', help='Port to listen on', default = 1337, type = int)
    parser.add_argument('--OpenLPUsername', help='Username to log into OpenLP as', default = "openlp")
    parser.add_argument('--OpenLPPassword', help='Password to log into OpenLP as', default = "6d22f1af18ffd70")
    args = parser.parse_args()

    # print(f"args is: {args}")

    print("Starting up OpenLP OSC -> REST converter")

    authentication = OLP.OpenLPAuthentication(args.OpenLP_REST_URL,args.OpenLPUsername,args.OpenLPPassword)

    # NOTE: Because OpenLP seems to start slowly, don't grab an initial auth token at program startup
    # auth_token = authentication.getAuthenticationToken()
    # print ("Received auth token:",auth_token)

    openLP = OLP.OpenLP(authentication)

    dispatcher = Dispatcher()
    dispatcher.map("/OpenLP/core/display", OpenLP_core_display)
    dispatcher.map("/OpenLP/controller/progress", OpenLP_controller_progress)
    dispatcher.set_default_handler(default_handler)

    ip = args.ListenIP
    port = args.ListenPort

    print ("Listening on IP:",ip)
    print ("Listening on Port:",port)

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

def OpenLP_core_display(address, *args):
    global openLP
    print(f"core_display: {address}: {args}")
    openLP.core_display(args[0])

def OpenLP_controller_progress(address, *args):
    global openLP
    print(f"core_progress: {address}: {args}")
    openLP.controller_progress(args[0])

# def print_handler(address, *args):
#     global openLP
#     print(f"{address}: {args}")
#
def default_handler(address, *args):
    global openLP
    print(f"DEFAULT (unhandled): {address}: {args}")



if __name__ == "__main__":
    main()
