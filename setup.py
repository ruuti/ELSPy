from setuptools import setup, find_packages

def parse_requirements(filename):
  """ load requirements from a pip requirements file """
  lineiter = (line.strip() for line in open(filename))
  return [line for line in lineiter if line and not line.startswith("#")]

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='ELSPy',
  version='0.1.1',
  scripts=['elspy.py'] ,
  author="Miikka Värri",
  author_email="miikka.varri@gmail.com",
  description="Electrolux Laundry System Python utility package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/ruuti/ELSPy",
  install_requires=parse_requirements('requirements.txt'),
  classifiers=[
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
  ],
 )