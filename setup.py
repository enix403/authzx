import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="authzx-enix403",
    version="0.0.1",
    author="Radium",
    author_email="fog.code000@gmail.com",
    description="A library to manage authorization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enix403/authzx",
    project_urls={
        "Bug Tracker": "https://github.com/enix403/authzx/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)