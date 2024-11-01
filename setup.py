from setuptools import setup, Extension
from Cython.Build import cythonize
import os
from pathlib import Path


# Define Cython extensions
extensions = [Extension("greety.example", ["greety/example.py"])]

""" init_path = Path(__file__).parent / "greety" / "__init__.py"

with open(init_path) as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break
    else:
        raise RuntimeError("Unable to find version string.") """

setup(
    name="greety",
    version="0.2.13",
    author="Charles Dhainaut",
    author_email="ch.dhainaut@gmail.com",
    description="A sample package compiled with Cython",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["greety"],
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    include_package_data=False,
    zip_safe=False,
)
