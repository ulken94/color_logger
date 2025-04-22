import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="color_logger",
    version="0.1.0",
    author="ulken94",
    author_email="bestwook7@gmail.com",
    description="Pretty colored logger for python.",
    long_description=long_description,
    long_description_content_type="test/markdown",
    url="https://github.com/ulken94/color_logger.git",
    clasifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
