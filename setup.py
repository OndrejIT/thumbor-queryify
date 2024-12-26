# Author Ondrej Barta
# git@ondrej.it
# Copyright 2024

from distutils.core import setup

from thumbor_queryify import __version__

TESTS_REQUIREMENTS = []

setup(
    name="thumbor-queryify",
    version=__version__,
    description="",
    long_description="",
    keywords=["thumbor url query handler"],
    author="Ondrej Barta",
    author_email="git@ondrej.it",
    url="https://github.com/OndrejIT/thumbor-queryify",
    license="MIT",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
    packages=[
        "thumbor_queryify.handlers",
    ],
    package_dir={"thumbor_queryify": "thumbor_queryify"},
    include_package_data=True,
    package_data={"": ["*.xml"]},
    install_requires=[
        "thumbor>=7.0.0",
    ],
    extras_require={"tests": TESTS_REQUIREMENTS},
    entry_points={
        "console_scripts": [],
    },
)
