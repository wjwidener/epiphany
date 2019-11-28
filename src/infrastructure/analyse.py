def init(sub_parser):
    sub_parser = sub_parser.add_parser('analyse', description='Analyse user provided infrastructure')
    sub_parser.set_defaults(func=run)

def run(args):
    print('Running infra analyse')   
    return 0