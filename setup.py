import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LayeredEncode",
    version="0.0.1",
    author="RannStudio",
    description="Encode your python script in layers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rann-Studio/LayeredEncode",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)