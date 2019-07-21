from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="zookeeper",
    version="0.0.1",
    author="Alejandro D Pages",
    author_email="apages2@unl.edu",
    description="Zooniverse data management tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alejandropages/Zookeeper.git",
    packages=find_packages(),
    install_requires=['click', 'panoptes-client'],
    entry_points={
        'console_scripts':['zookeeper = zookeeper.cli:start']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
