import setuptools

with open('README.md', 'r') as readMe:
    long_description = readMe.read()

setuptools.setup(

    name = 'self_concepts',
    version = '1.0',
    author = 'Grady Booch',
    author_email = 'egrady@booch.com',
    description = 'Self''s foundational abstractions',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = 'self agi neuro-symbolic',
    url = 'https://github.com/booch-self/self-concepts',
    packages = ['self_concepts'],
    package_dir = ['self_concepts': 'source/python'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.8'

)
