import click

from isotl.tools.index import index


@click.group()
def cli():
    pass


@cli.command('index',
             help="Index an ISO files")
@click.argument('path',
                type=click.Path(exists=True),
                required=True,
                default='.',)
def index(path):
    print("Hello from index command!, root_path: ", path)
    pass


if __name__ == '__main__':
    cli()
