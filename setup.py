from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jsonl_validator',
    version='0.1.0',
    author='Eugene Evstafev',
    author_email='hi@eugene.plus',
    description='A simple library to validate JSON Lines (jsonl) formatted strings.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/jsonl_validator',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'jsonlines>=3.0.0',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    license='MIT',
)