from setuptools import setup, find_packages

setup(
    name="jwt-inspector-cli",
    version="1.0.0",
    description="A CLI tool to decode, validate, and analyze JSON Web Tokens.",
    author="Prudence",
    author_email="cyberprudie@gmail.com",
    packages=find_packages(),
    install_requires=[
        "PyJWT==2.8.0",
        "click==8.1.7"
    ],
    entry_points={
        "console_scripts": [
            "jwt-inspector=src.main:cli"
        ]
    },
    keywords=["JWT", "CLI", "token", "inspector"],
    license="MIT",
    python_requires=">=3.6"
)