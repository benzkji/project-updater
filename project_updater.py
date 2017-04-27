import os

import click
import subprocess

@click.command()
@click.option('--name', help='Name of your update. Example: update-4.7', required=True)
@click.option('--tag-prefix', default='', help='Prefix for your update tags. Example: update-4.7-')
@click.option('--project-path', default='.', help='Root path of project, if not .',)
@click.option('--start-after', help='Start after this step.')
@click.option('--silent', help='Always yes, no breaks.')
def updater(name, tag_prefix, project_path, start_after, silent):
    """
    help for step by step updating a (django) project.

    """
    if not tag_prefix:
        tag_prefix = name
    click.echo("-----------------------------------")
    click.echo("#### Fetching tags with prefix \"%s\"" % tag_prefix)
    try:
        tags = subprocess.check_output('cd %s && git tag | grep %s' % (project_path, tag_prefix), shell=True)
    except subprocess.CalledProcessError as e:
        if e.output:
            click.echo(e.output)
        else:
            click.echo("Error getting tags, aborting!")
        exit()
    tags = tags.splitlines()
    # check if current tag is in taglist, if yes, start from there onwards
    current_tag = None
    if start_after:
        current_tag = start_after
    else:
        try:
            current_tag = subprocess.check_output('cd %s && git describe' % project_path, shell=True)
        except subprocess.CalledProcessError as e:
            current_tag = ''
    current_tag = current_tag.strip()
    if current_tag in tags:
        while not tags[0] == current_tag.strip(): tags.pop(0)
        tags.pop(0)
        click.echo("-----------------------------------")
        click.echo("#### Starting right after %s" % current_tag)
    for tag in tags:
        click.echo("-----------------------------------")
        click.echo("#### To step %s" % tag)
        try:
            git_out = subprocess.check_output('cd %s && git checkout %s' % (project_path, tag), shell=True)
        except subprocess.CalledProcessError as e:
            click.echo('Tag not found, aborting: %s' % tag)
            exit()

        try:
            command = os.path.join(project_path, name, tag + ".sh")
            if os.path.isfile(command):
                subprocess.call(command)
            else:
                click.echo("No script for %s. Going ahead." % tag)
            # click.echo(command)
        except subprocess.CalledProcessError as e:
            if e.output:
                click.echo(e.output)
            else:
                click.echo("Unknown error running %s!" % command)
            exit()
        has_break = os.path.join(project_path, name, tag + ".break")
        if os.path.isfile(has_break):
            click.echo("-----------------------------------")
            click.echo("#### Hasta la vista. Break after %s" % tag)
            click.echo("-----------------------------------")
            exit(0)
    click.echo("-----------------------------------")


if __name__ == '__main__':
    updater()
