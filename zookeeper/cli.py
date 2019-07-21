'''
NOTE:
    This utility is deprecated, please use the official Zooniverse project
    management cli tool Panoptes.

DESC:
    Schnablelab Zooniverse project management tool

DEPENDENCIES:
    click,
    panoptes-client
'''

import click

@click.group()
@click.option('-u', '--username', help='zooniverse username or email', default=None)
@click.option('-p', '--password', help='password', default=None)
@click.pass_context
def Zookeeper(ctx, username, password):
    ''' Zooniverse project data management tools '''
    ctx.obj['un'] = username
    ctx.obj['pw'] = password
    pass


from .commands import (
    upload,
    export,
    manifest
)


Zookeeper.add_command(upload)
Zookeeper.add_command(export)
Zookeeper.add_command(manifest)


def start():
    Zookeeper(obj={})

if __name__ == '__main__':
    start()
