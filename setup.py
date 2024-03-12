from setuptools import setup 
import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR = "pykhaleda"
SRC_REPO = "ccnClassifier"
AUTHOR_EMAIL = "khaledalzebibi1@gmail.com"


setup(
    name=REPO_NAME,
    version=__version__,
    description="A sample Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
)

