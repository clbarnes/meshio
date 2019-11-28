import itertools
import os
import runpy

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = runpy.run_path(os.path.join(base_dir, "meshio", "__about__.py"))

extras = {
    "exodus": ["netCDF4"],
    "hdf5": ["h5py"],  # MED, MOAB, XDMF formats
    "xml": ["lxml"],  # Dolfin, VTU, XDMF, SVG
}

extras["all"] = list(itertools.chain.from_iterable(extras.values()))


setup(
    name="meshio",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=find_packages(),
    description="I/O for various mesh formats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nschloe/meshio",
    project_urls={
        "Code": "https://github.com/nschloe/meshio",
        "Issue tracker": "https://github.com/nschloe/meshio/issues",
    },
    license=about["__license__"],
    platforms="any",
    install_requires=["numpy"],
    python_requires=">=3",
    extras_require={
        "all": ["netCDF4", "h5py", "lxml"],
        "exodus": ["netCDF4"],
        "hdf5": ["h5py"],  # MED, MOAB, XDMF formats
        "xml": ["lxml"],  # Dolfin, VTU, XDMF, SVG
    },
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    entry_points={
        "console_scripts": [
            "meshio-convert = meshio._cli:convert",
            "meshio-info = meshio._cli:info",
        ]
    },
)
