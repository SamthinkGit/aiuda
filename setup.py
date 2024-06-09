from setuptools import find_packages
from setuptools import setup

setup(
    name='aiuda',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    author='Sebastian Mayorquín',
    author_email='sebastianmayorquin@gmail.com',
    description='AI tools for runtime python. Such as advanced pprinting, tree, formatting and some random utils.',
    url='https://github.com/SamthinkGit/aiuda',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
