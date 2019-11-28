def init(sub_parser):
    sub_parser = sub_parser.add_parser('create', description='Create the Epiphany repository')
    sub_parser.set_defaults(func=run)

def run(args):
    print('Running repo create')
    return 0   