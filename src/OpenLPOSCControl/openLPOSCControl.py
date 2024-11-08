#! /usr/bin/env python3

# from typing import Any, Dict

import argparse
import configparser
import logging

from cysystemd import journal
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

from OpenLPOSCControl import OpenLPRestAPI as OLP

global openLP

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.addHandler(journal.JournaldLogHandler())


def main():
    global openLP

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--OpenLP_REST_URL",
        help="URL for OpenLP REST API",
    )
    parser.add_argument("--ListenIP", help="IP address to listen on")
    parser.add_argument(
        "--ListenPort", help="Port to listen on", type=int, default=1337
    )
    parser.add_argument(
        "--OpenLPAuthenticationEnabled",
        type=bool,
        help="Is OpenLPAuthentication Enabled",
    )
    parser.add_argument("--OpenLPUsername", help="Username to log into OpenLP")
    parser.add_argument("--OpenLPPassword", help="Password to log into OpenLP")
    parser.add_argument(
        "--OpenLPConfigurationFile",
        help="OpenLP configuration file, try reading the values directly",
        # default="~/.config/openlp.org.conf",
        default="/home/fprice/.config/openlp.org.conf",
    )
    args = parser.parse_args()

    # print(f"args is: {args}")

    logger.info("Starting up OpenLP OSC -> REST converter")

    if args.OpenLPConfigurationFile is not None:
        logger.info(
            f"Attempting to read OpenLP configuration file at [{args.OpenLPConfigurationFile}]"
        )
        config = configparser.ConfigParser()
        config.read(args.OpenLPConfigurationFile)

        # print(f"Sections: {config.sections()}")

        ipAddress = config["api"]["ip%20address"]
        if args.OpenLPAuthenticationEnabled is None:
            args.OpenLPAuthenticationEnabled = config["api"]["authentication%20enabled"]
        userID = config["api"]["user%20id"]
        password = config["api"]["password"]

        # We listen on the same IP as OpenLP to keep things simple
        if args.ListenIP is None:
            args.ListenIP = ipAddress

        # use OpenLP values as defaults
        if args.OpenLP_REST_URL is None:
            if args.ListenIP == "0.0.0.0":
                logger.info(
                    f"Can's use ListenIP of 0.0.0.0 to talk to OpenLP, switching to localhost."
                )
                args.OpenLP_REST_URL = "http://127.0.0.1:4316/"
            else:
                args.OpenLP_REST_URL = f"http://{args.ListenIP}:4316/"

        if args.OpenLPAuthenticationEnabled:
            if args.OpenLPUsername is None:
                args.OpenLPUsername = userID
            if args.OpenLPPassword is None:
                args.OpenLPPassword = password

    else:
        if args.ListenIP is None:
            args.ListenIP = "127.0.0.1"
        if args.OpenLP_REST_URL is None:
            args.OpenLP_REST_URL = "http://{args.ListenIP}:4316/"

    logger.info(f"Our Listen IP Address: {args.ListenIP}")
    logger.info(f"Our Listen Port: {args.ListenPort}")
    logger.info(f"OpenLP AuthenticationEnabled: {args.OpenLPAuthenticationEnabled}")
    logger.info(f"OpenLP userID: {args.OpenLPUsername}")
    logger.info(f"OpenLP password: {args.OpenLPPassword}")
    logger.info(f"OpenLP REST URL: {args.OpenLP_REST_URL}")

    authentication = OLP.OpenLPAuthentication(
        args.OpenLP_REST_URL, args.OpenLPUsername, args.OpenLPPassword
    )

    # NOTE: Because OpenLP seems to start slowly, don't grab an initial
    # auth token at program startup
    # auth_token = authentication.getAuthenticationToken()
    # print ("Received auth token:",auth_token)

    openLP = OLP.OpenLP(authentication)

    dispatcher = Dispatcher()
    dispatcher.map("/OpenLP/core/display", OpenLP_core_display)
    dispatcher.map("/OpenLP/controller/progress", OpenLP_controller_progress)
    dispatcher.set_default_handler(default_handler)

    ip = args.ListenIP
    port = args.ListenPort

    logger.info(f"Listening on IP: {ip}")
    logger.info(f"Listening on Port: {port}")

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
    logger.info(f"core_display: {address}: {args}")
    openLP.core_display(args[0])


def OpenLP_controller_progress(address, *args):
    global openLP
    logger.info(f"core_progress: {address}: {args}")
    openLP.controller_progress(args[0])


# def print_handler(address, *args):
#     global openLP
#     print(f"{address}: {args}")
#
def default_handler(address, *args):
    global openLP
    logger.info(f"DEFAULT (unhandled): {address}: {args}")


if __name__ == "__main__":
    main()
