from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
from pathlib import Path


def get_ext_paths(root_dir):
    return list(Path(root_dir).rglob("*.py"))


# Define the root directory for the package
package_dir = Path(__file__).parent / "greety"
# Get paths of all .py files in the directory
extension_sources = get_ext_paths(package_dir)

# Create a single Cython extension
ext_modules = [
    Extension(
        "greety",  # Name of the compiled module
        sources=[str(src) for src in extension_sources],
        include_dirs=[str(package_dir)],
    )
]

# Compile the extension using Cython
ext_modules = cythonize(ext_modules, compiler_directives={"language_level": "3"})

setup(
    name="greety",
    version="0.2.14",
    author="Charles Dhainaut",
    author_email="ch.dhainaut@gmail.com",
    description="A sample package compiled with Cython",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=[],  # Keep it empty to avoid packaging source files
    ext_modules=ext_modules,
    include_package_data=False,
    zip_safe=False,
)
