def init(sub_parser):
    sub_parser = sub_parser.add_parser('prepare', description='Returns a bundle of files to create an offline repository')
    sub_parser.set_defaults(func=run)

def run(args):
    print('Running repo prepare')
    return 0  