from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="memebayes",
    version="0.2.1",
    author="TheJPMZ",
    author_email="monzon.jpmz@gmail.com",
    description="A bayesian network implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheJPMZ/memebayes",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=['bayesian', 'network', 'machine learning', 'data science']
)
