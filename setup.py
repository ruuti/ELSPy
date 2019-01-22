from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='ELSPy',
  version='0.1',
  scripts=['elspy.py'] ,
  author="Miikka Värri",
  author_email="miikka.varri@gmail.com",
  description="Electrolux Laundry System Python utility package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/ruuti/ELSPy",
  install_requires=[
    'zeep>=3.2.0'
  ],
  classifiers=[
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
  ],
 )