from setuptools import setup


# hope this works
# http://click.pocoo.org/5/setuptools/#scripts-in-packages
setup(
    name='project_updater',
    version='0.1',
    py_modules=['project_updater', 'south2django', ],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        project_updater=project_updater:project_updater
        south2django=south2django:south2django
    ''',
)