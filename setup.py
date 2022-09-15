from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tarozi_syncer/__init__.py
from tarozi_syncer import __version__ as version

setup(
	name="tarozi_syncer",
	version=version,
	description="Tarozy api syncer",
	author="Sepand.Y",
	author_email="sepand_y@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
