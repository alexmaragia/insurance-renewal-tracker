import click
from .helpers import manage_policies, manage_clients, view_reminders

@click.group()
def cli():
    """Insurance Renewal Tracker CLI"""
    pass

@cli.command()
def policies():
    """Manage policies"""
    manage_policies()

@cli.command()
def clients():
    """Manage clients"""
    manage_clients()

@cli.command()
def reminders():
    """View reminders"""
    view_reminders()

if __name__ == '__main__':
    cli()