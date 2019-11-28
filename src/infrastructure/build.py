def init(sub_parser):
    sub_parser = sub_parser.add_parser('build', description='Build/Modify infrastructure on a supported cloud provider')
    sub_parser.set_defaults(func=run)

def run(args):
    print('Running infra build')
    return 0   