import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utree",
    version="0.0.1",
    author="Trelent Inc.",
    author_email="contact@trelent.net",
    description="A high-level syntax tree parser for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trelent/utree",
    project_urls={
        "Bug Tracker": "https://github.com/trelent/utree/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "tree-sitter"
    ],
)
