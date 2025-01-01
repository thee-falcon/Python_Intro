import setuptools
from pathlib import Path

setuptools.setup(
    name="thefalconPDF",
    version= 1.0,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["data", "tests"]),
    )

# to generate a disribuion package:
# open the terminal and run:
#                          setup.py sdst bdist_wheel

#                          meaning of this commands:
#                          sdst: which is short for source distribution
#                          bdist_wheel: which is short for build distribution
# so with this commands we're going generate two distribution packages.
# and the final step is to upload them to pypi.org.
# use command: 
#            twine upload dist/*