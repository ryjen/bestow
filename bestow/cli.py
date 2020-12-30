import subprocess
import click
from .context import Context


@click.command()
@click.argument("parmeters", nargs=-1)
def cli(parameters):

    ctx = Context(parameters)

    ctx.process()

    return subprocess.call(ctx.executable())
