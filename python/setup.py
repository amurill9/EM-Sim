import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EM_Sim", 
    version="0.0.2",
    author="EM.py-r3-CAL()",
    # author_email="",
    description="EM_Sim: Electromagnetic Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amurill9/EM-Sim",
    platforms=['Windows', 'Linux', 'Mac OS-X'],
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    python_requires='>=3.6',
)
