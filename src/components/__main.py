#!/usr/bin/env py
from core import module

info = lambda: None
info.MODULE_NAME = 'components'
info.MODULE_VERSION = '1.0.0'
info.MODULE_DESCIPTION = 'Module to manage components'
info.MODULE_CLI_NAME = 'components'

def init(parser):
    return module.init(info, parser)

def run():
    module.run(info)

if __name__ == '__main__':
    run()  