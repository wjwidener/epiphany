def init(sub_parser):
    sub_parser = sub_parser.add_parser('template', description='Defines a new repository template')
    sub_parser.set_defaults(func=run)    

def run(args):
    print('Running repo template') 
    return 0  