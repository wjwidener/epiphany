import infrastructure.build
import repository.create, repository.teardown
import components.apply

def init(sub_parser):
    sub_parser = sub_parser.add_parser('apply', description='Creates/modifies an Epiphany cluster')
    sub_parser.set_defaults(func=run)    

def run(args):
    infrastructure.build.run(args)
    repository.create.run(args)
    components.apply.run(args)
    repository.teardown.run(args)
    return 0  