from setuptools import setup
from setuptools import find_packages

with open('README.rst',encoding= 'UTF 8') as f :
    readme=f.read()

setup(
       #name of the package
        name='pgbackup',
        #version of the package
        version= '0.1.0',
        #description of the package
        description = 'DATABASE Backup locally or S3',
        #lonf description -  through the README.rst documentation
        long_description = readme,
        #author of the package
        author='DevD003',
        #email of the author
        author_email='adithyakesineni@gmail.com',
        #the dependedncies are mentioned here in [], empty - currently
        install_requires=[],
        #finds the packages,recursively for __init__.py
        packages=find_packages('src'),
        #creating a dictionary - point from empty string to src
        #<< A legacy thing from diskutils - needed since we mentioned the src folder >>
        package_dir = { '' : 'src' }

    )



