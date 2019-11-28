def init(sub_parser):
    sub_parser = sub_parser.add_parser('teardown', description='Disables the Epiphany repo')
    sub_parser.set_defaults(func=run)

def run(args):
    print('Running repo teardown')
    return 0  