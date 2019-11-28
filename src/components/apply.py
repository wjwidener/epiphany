def init(sub_parser):
    sub_parser = sub_parser.add_parser('apply', description='Apply components to Epiphany infrastructure')
    sub_parser.set_defaults(func=run)

def run(args):
    print('Running components apply')
    return 0   