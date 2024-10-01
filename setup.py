from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='BCONVERT',
    version='0.1.0',
    author='Groupe 1',  
    author_email='', 
    description='A project to convert data (NSI project)',  
    url='https://github.com/El1teW0lf/2024_2025__p04_projet1_gp1',  
    packages=find_packages(),  
    install_requires=required, 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
