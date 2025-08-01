from setuptools import setup, find_packages

setup(
    name='DocXtract',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'lxml'
        
    ],
    author='Rohit Chauhan',
    author_email='rohitchauhan2185@gmail.com',
    description='Extract text and image paths from DOCX files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Thakur-Rohit-chauhan/Pydocx',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
