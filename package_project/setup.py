from setuptools import find_packages, setup

long_desc = """
This package is created for use of the ....."""

setup(
    name='example777',
    packages=find_packages(include=['example777']),
    version='0.1.0',
    description='Test package to demonstrate how to build packages',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    author='M.O.',
    license='MIT',
    install_requires=[], # Dependencies
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.2'],
    test_suite='tests'
)
