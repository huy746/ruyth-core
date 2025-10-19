from setuptools import setup, find_packages

setup(
    name="ruythcore",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "websockets"
    ],
    entry_points={
        "console_scripts": [
            "ruythcore=ruythcore.client:main"
        ]
    }
)
