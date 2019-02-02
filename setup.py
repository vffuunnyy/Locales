from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Locales",
    version="0.0.1",
    author="vffuunnyy",
    author_email="vffuunnyy@gmail.com",
    description="Module for multilingual solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vffuunnyy/Locales",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
