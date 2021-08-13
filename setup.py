from setuptools import setup
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'easy_exchange_rates',         # How you named your package folder (MyLib)
    packages = ['easy_exchange_rates'],   # Chose the same as "name"
    version = '0.1.2',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Easy abstraction to get currency exchange data from https://exchangerate.host/ to a pandas dataframe',   # Give a short description about your library
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Odd Gunnar Aspaas',                   # Type in your name
    author_email = 'odd.learning@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/oddaspa/easy-exchange-rates',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/oddaspa/easy-exchange-rates/archive/refs/tags/v0.1.2-alpha.tar.gz',    # I explain this later on
    keywords = ['Currency Exchange', 'pandas', 'API'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)