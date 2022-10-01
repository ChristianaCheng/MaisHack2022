from setuptools import setup, find_packages

setup(
    name="mais_hack",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    description="A python package for working on Mais Hack 2022",
    url="https://github.com/ChristianaCheng/MaisHack2022",
    author="Caleb Moses",
    author_email="caleb.moses@mcgill.mail.ca",
    include_package_data=True,
)
