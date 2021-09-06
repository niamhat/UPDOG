import setuptools


setuptools.setup(
    name='pyupdog',
    version='1.0.6',
    author='Joseph Halstead',
    author_email='josephhalstead89@gmail.com',
    description='Python program for calculating UPD',
    long_description='test',
    long_description_content_type='text/markdown',
    url='https://github.com/josephhalstead/pyvariantfilter',
    packages=setuptools.find_packages(),
    scripts= ['UPDog.py'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
   'pysam>=0.16',
   'pandas>=1.3.2',
   'seaborn>=0.10.1',
   'scipy>=1.4.1',
   'pyvariantfilter>=1.0.4',
   'numpy>=1.18.1'
],
)
