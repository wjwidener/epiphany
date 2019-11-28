def init(sub_parser):
    sub_parser = sub_parser.add_parser('delete', description='Delete infrastructure on a supported cloud provider')
    sub_parser.set_defaults(func=run)

def run(args):
    print('Running infra delete') 
    return 0  