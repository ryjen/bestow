from setuptools import setup

setup(
    name="bestow",
    version="0.0.1",
    description="A casing for GNU stow and dotfile management",
    author="Ryan Jennings",
    author_email="ryan@micrantha.com",
    license="Proprietary",
    packages=["bestow", "tests"],
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
