# pylint: disable = C0111
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    DESCRIPTION = f.read()

setup(
    name="txtmarker",
    version="1.1.0",
    author="NeuML",
    description="Finds and highlights text in documents",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/neuml/txtmarker",
    project_urls={
        "Documentation": "https://github.com/neuml/txtmarker",
        "Issue Tracker": "https://github.com/neuml/txtmarker/issues",
        "Source Code": "https://github.com/neuml/txtmarker",
    },
    license="Apache 2.0: http://www.apache.org/licenses/LICENSE-2.0",
    packages=find_packages(where="src/python"),
    package_dir={"": "src/python"},
    keywords="pdf highlight text search",
    python_requires=">=3.9",
    install_requires=["pdfminer.six>=20201018", "pdf-annotate>=0.11.0"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
)
