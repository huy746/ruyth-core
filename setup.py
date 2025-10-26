# setup.py
from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="ruythcore",
    version="1.0.0",
    description="RuythCore — lightweight Discord-like bot core, not based on discord.py",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/huy746/ruyth-core",
    author="ruythbot_huy",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0"
    ],
    python_requires=">=3.8",
    license="MIT",
)
