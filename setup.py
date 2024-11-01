from setuptools import setup, Extension
from Cython.Build import cythonize
import os
from greety import __version__

# Define Cython extensions
extensions = [Extension("greety.example", ["greety/example.py"])]

setup(
    name="greety",
    version=__version__,
    author="Charles Dhainaut",
    author_email="ch.dhainaut@gmail.com",
    description="A sample package compiled with Cython",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["greety"],
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    include_package_data=True,
    zip_safe=False,
)
