def init(sub_parser):
    sub_parser = sub_parser.add_parser('template', description='Defines components template')
    sub_parser.set_defaults(func=run)    

def run(args):
    print('Running components template') 
    return 0  