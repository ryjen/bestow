from setuptools import setup, find_packages

setup(
    name="bestow",
    version="0.0.1",
    description="A casing for GNU stow and dotfile management",
    author="Ryan Jennings",
    author_email="ryan@micrantha.com",
    license="GNU v3",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'click',
    ],
    entry_points='''
      [console_scripts]
      bestow=bestow:cli
    ''',
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suit="tests",
)
