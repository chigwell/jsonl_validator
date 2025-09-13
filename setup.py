from setuptools import setup, find_packages
import os

# Read the README file for the long description
HERE = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A simple library to validate JSON Lines (jsonl) formatted strings."

setup(
    name='jsonl_validator',
    version='0.1.0',  # You can set a specific version here
    author='Eugene Evstafev',
    author_email='hi@eugene.plus',
    description='A simple library to validate JSON Lines (jsonl) formatted strings.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/jsonl_validator',
    packages=find_packages(where='jsonl_validator'), # Assuming your package is in a 'jsonl_validator' directory
    package_dir={'': 'jsonl_validator'}, # Map the package directory
    install_requires=[
        'jsonlines', # Added jsonlines as it was imported in the source code
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',  # Adjust as needed (e.g., '4 - Beta', '5 - Production/Stable')
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: General',
    ],
    python_requires='>=3.7', # Based on the classifiers, Python 3.7+ is supported
    license='MIT',
    # If you have tests, uncomment and configure:
    # tests_require=['unittest'],
    # test_suite='test',
)