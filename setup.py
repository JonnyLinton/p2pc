from setuptools import setup

setup(
    name='p2pc',
    py_modules=['p2pc'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        p2pc=p2pc:run
    ''',
)
