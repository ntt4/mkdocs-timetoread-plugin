from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='mkdocs-timetoread-plugin',
    version='0.0.4',
    description='"Estimated Time To Read" generator for MkDocs',
    long_description=long_description,
    long_description_content_type='text/markdown',
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

