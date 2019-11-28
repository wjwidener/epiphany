import infrastructure.template
import repository.template
import components.template

def init(sub_parser):
    sub_parser = sub_parser.add_parser('template', description='Generates templates for infrastructure, repo and components')
    sub_parser.set_defaults(func=run)    

def run(args):
    infrastructure.template.run(args)
    repository.template.run(args)
    components.template.run(args)
    return 0  