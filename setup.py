from setuptools import setup
import os

VERSION = "0.2a"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-column-inspect",
    description="Experimental Datasette plugin for inspecting columns",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-column-inspect",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_column_inspect"],
    entry_points={"datasette": ["column_inspect = datasette_column_inspect"]},
    install_requires=[
        "datasette",
    ],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx", "sqlite-utils"]},
    tests_require=["datasette-column-inspect[test]"],
    package_data={"datasette_column_inspect": ["templates/*.html"]},
)
