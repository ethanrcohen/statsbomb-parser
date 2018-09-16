import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()


with open('requirements.txt') as f:
    text = f.read().split()
    packages = [i.split('==')[0] for i in text]


setuptools.setup(
    name='statsbomb',
    version='0.1.1',
    author='Imran Khan',
    author_email='imrankhan17@hotmail.co.uk',
    description='A Python package to parse StatsBomb json data to csv',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/imrankhan17/statsbomb',
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=packages,
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)