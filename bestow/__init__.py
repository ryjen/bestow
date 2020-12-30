"""A module for adding functionality to GNU stow"""
import click
from .controller import Controller
from .context import Context


@click.command()
@click.argument("parameters", nargs=-1)
def cli(parameters) -> int:
    """Entry point for the command line"""

    ctx = Context(parameters)

    controller = Controller(ctx)

    try:
        controller.load()
        return controller.execute()
    finally:
        controller.unload()
