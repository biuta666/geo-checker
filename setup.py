from setuptools import setup

setup(
    name="geo-checker",
    version="0.1.0",
    description="Scan your brand's AI presence in one command",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="biuta666",
    author_email="ieqqnet@163.com",
    url="https://github.com/biuta666/geo-checker",
    py_modules=["geo_checker"],
    install_requires=["httpx"],
    entry_points={
        "console_scripts": [
            "geo-checker=geo_checker:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    ],
    python_requires=">=3.9",
)
