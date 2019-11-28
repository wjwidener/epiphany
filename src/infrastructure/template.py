def init(sub_parser):
    sub_parser = sub_parser.add_parser('template', description='Defines a new infrastructure template')
    sub_parser.set_defaults(func=run)    

def run(args):
    print('Running infra template') 
    return 0  