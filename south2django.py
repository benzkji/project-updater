import fnmatch
import os

import click
import subprocess
import glob

import shutil


@click.command()
@click.option('--project-path', default='./', help='Root path of project, if not .',)
def south2django(project_path):
    """
    recursivly rename migrations to south_migrations, add migrations folder with __init__.py

    """
    # works. thx.
    # http://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python
    migration_folders = [os.path.join(dirpath, dir)
        for dirpath, dirnames, files in os.walk(project_path)
        for dir in fnmatch.filter(dirnames, 'migrations')]
    for folder in migration_folders:
        rename = folder.replace('migrations', 'south_migrations')
        init_py = os.path.join(folder, '__init__.py')
        if os.path.isdir(rename):
            click.echo("skipping (south_migrations exists) '%s'" % folder)
            continue
        try:
            shutil.move(folder, rename)
        except shutil.Error:
            print "error renaming '%s'" % folder
            continue
        os.mkdir(folder)
        open(init_py, 'a').close()
        print "moved '%s'" % folder


if __name__ == '__main__':
    south2django()
