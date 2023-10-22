from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.2",
    author="abhishekjadhav3470",
    description="A tiny package for ANN Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhishekjadhav3470/ANN-Implementation-by-DLCVNLP.git",
    author_email="abhishekjadhav3470@gmail.com",
    packages=["src"],
    python_requires=">=3.9",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)