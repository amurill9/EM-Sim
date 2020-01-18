import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EM-Sim", 
    version="0.0.2",
    author="EM.py-r3-CAL()",
    # author_email="",
    description="Electromagnetic Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amurill9/EM-Sim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
