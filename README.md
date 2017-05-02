
# Project updater

Automating your painfully crafted update routines. Created for updating my django projects, could be used otherwise. Contains a helper for migrating
from south to django migrations (south2django).

## Install

    pip install -e git+https://github.com/benzkji/project-updater

## Usage

### project_updater

For bigger updates, you would probably create a branch `update-xy`. Start your update work. At every step where you
need some shell scripts executet, create a tag, for example `update-xy-1`. In your project dir, have a folder `update-xy`,
therein, place a file `update-xy-1.sh`. This shell script will be executed in the automated udpate process.

    cd to_your_project_root
    project_updater --name=update-7.2

What it does:
    - Get all tags that start with `update-7.2`
    - For every tag found, execute it's script if available
    - If there is a `tagname.break` file found, execution is aborted, for manual hands on
    - If at startup, the current tag name matches a tag in the tag list, execution will start right after

Options:
    --name TEXT          Name of your update and folder where we'll look for shell scripts. Example: update-4.7.   [required]
    --tag-prefix TEXT    Prefix of your update tags. If empty, name is used. Example: update-4.7-
    --project-path TEXT  Root path of project, if not `.`
    --start-after TEXT   Start after this step/tag.
    --silent TEXT        Always yes, no breaks.
    --help               Show this message and exit.


### south2django

recursivly rename `migrations` to `south_migrations`, add `migrations` folder with `__init__.py`, for a fresh start with django
1.7+.