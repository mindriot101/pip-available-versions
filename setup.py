from setuptools import setup

setup(
    py_modules=['pip_versions_available'],
    name='pip_versions_available',
    author='Simon Walker',
    author_email='s.r.walker101@googlemail.com',
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pip-versions-available=pip_versions_available:__main__',
        ],
    },
)
