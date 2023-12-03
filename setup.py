from setuptools import setup, find_packages


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()


def read_file(file):
    with open(file) as f:
        return f.read()


requirements = read_requirements("requirements.txt")

setup(
    name='nexitor',
    version='0.0.0',
    author='Tarik Gün (tarik56)',
    url='https://github.com/tarik56/nexitor.python',
    description='Python Flask, Django and FastApi integration client for Nexitor',
    long_description_content_type="text/markdown",
    long_description="",
    license="MIT license",
    packages=['nexitor'],
    package_dir={'': 'src'},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
