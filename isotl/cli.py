import click

from isotl.commands.index import index


@click.group()
def cli():
    pass


cli.add_command(index)

if __name__ == '__main__':
    cli()
