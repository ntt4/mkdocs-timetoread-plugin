from setuptools import setup, find_packages

setup(
    name='mkdocs-timetoread-plugin',
    version='0.0.1',
    description='"Estimated Time To Read" generator for MkDocs',
    long_description="mkdocs-timetoread-plugin is a lightweight 'estimated time to read' generator for MkDocs inspired by @alanhamlett's 'readtime' and Medium's read time formula.",
    keywords='mkdocs',
    url='https://github.com/ntt4/mkdocs-timetoread-plugin',
    author='Tavis Booth',
    author_email='code@entityfour.io',
    license='MIT',
    python_requires='>=3.7',
    install_requires=[
        'mkdocs>=1.3'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': ["timetoread = mkdocs_timetoread_plugin.plugin:TimeToRead"]}
    )

