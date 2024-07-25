import click


@click.command('index', help='Index an ISO file')
@click.argument('root_path', type=click.Path(exists=True), required=False)
def index(root_path):
    print("Hello from index command!, root_path: ", root_path)
    pass