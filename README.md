
# Project updater

Automating your painfully crafted update routines. Created for updating my django projects, could be used otherwise.
Workflow. safe version: Take website offline. Download all user generated content, ie /media/, for django, download
live database. Run updates on local machine. Upload db and media files again. Workflow, live version: Do it on your server.

## Install

    pip install project-updater

## Usage

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