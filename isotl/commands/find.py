import click


@click.command('find', help='Find an ISO file')
@click.argument('root_path', type=click.Path(exists=True), required=False)
def find(root_path):
    print("Hello from find command!, root_path: ", root_path)
    pass
