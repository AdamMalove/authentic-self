from setuptools import setup, find_packages

setup(
    name="authentic-self",
    version="1.0.2",
    description="52 questions to discover your authentic identity",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Adam Kucera",
    url="https://github.com/Adamkucera2/authentic-self",
    packages=find_packages(),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "authentic-self=authentic_self.generate_soul:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
