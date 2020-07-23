from setuptools import setup
from setuptools import find_packages

with open('README.md', 'r') as readMe:
    long_description = readMe.read()

setup(

    name = 'self_concepts',
    version = '1.0',
    author = 'Grady Booch',
    author_email = 'egrady@booch.com',
    description = 'Self''s foundational abstractions',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = 'self agi neuro-symbolic',
    url = 'https://github.com/booch-self/self-concepts',
    packages = find_packages(where='source'),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.8'

)
