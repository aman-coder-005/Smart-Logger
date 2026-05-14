from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smartlogger-aman", # Changed to be unique on PyPI
    version="0.1.0",
    description="A lightweight modular logging framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Aman Gupta",
    packages=find_packages(),
    python_requires=">=3.7",
)
