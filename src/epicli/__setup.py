from core.module import setup
from epicli import __main

if __name__ == '__main__':
    setup(__main.info, ['core', 'infrastructure', 'components', 'repository'])