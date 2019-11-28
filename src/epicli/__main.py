#!/usr/bin/env py
import sys
from core import module
import infrastructure.__main
import repository.__main
import components.__main
from epicli import apply 

info = lambda: None
info.MODULE_NAME = 'epicli'
info.MODULE_VERSION = '0.4.2'
info.MODULE_DESCIPTION = 'Main epicli module'
info.MODULE_CLI_NAME = 'epicli'

def init(info):
    # init epicli core modules
    parser, sub_parsers = module.init(info)

    # add external sub-modules
    infrastructure.__main.init(sub_parsers)
    repository.__main.init(sub_parsers)
    components.__main.init(sub_parsers)

    return parser, sub_parsers

def run():
    module.run(info, init)

if __name__ == '__main__':
    run()

