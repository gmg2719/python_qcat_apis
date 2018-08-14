import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QCAT_Basic",
    version="0.0.4",
    author="Weihua Chen",
    author_email="weihua.chen@gmail.com",
    description="A small package contains most useful QCAT interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weihuachen/python_qcat_apis",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ),
)
