import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matgrab",
    version="0.0.8",
    author="Aaronearlerichardson",
    author_email="jakdaxter31@gmail.com",
    description="search and extract field names or variables from MATLAB .mat files and return a pandas Dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aaronearlerichardson/matgrab",
    project_urls={
        "Bug Tracker": "https://github.com/Aaronearlerichardson/matgrab/issues",
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
